(() => {
  "use strict";
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [
    ...root.querySelectorAll(selector),
  ];
  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const header = $("#site-header");
  let scrollQueued = false;
  const updateHeader = () => {
    header.classList.toggle("scrolled", scrollY > 0);
    scrollQueued = false;
  };
  addEventListener(
    "scroll",
    () => {
      if (!scrollQueued) {
        requestAnimationFrame(updateHeader);
        scrollQueued = true;
      }
    },
    { passive: true },
  );
  updateHeader();

  const dropdowns = $$(".nav-dropdown");
  const menuTimers = new WeakMap();
  function closeMenu(menu) {
    if (!menu.open || menu.classList.contains("menu-closing")) return;
    menu.classList.add("menu-closing");
    menuTimers.set(
      menu,
      setTimeout(() => {
        menu.open = false;
        menu.classList.remove("menu-closing");
      }, 100),
    );
  }
  const closeMenus = (except) =>
    dropdowns.forEach((menu) => {
      if (menu !== except) closeMenu(menu);
    });
  dropdowns.forEach((menu) => {
    let timer;
    menu.addEventListener("toggle", () => {
      if (menu.open) closeMenus(menu);
    });
    menu.addEventListener("pointerenter", (event) => {
      if (
        event.pointerType === "mouse" &&
        matchMedia("(min-width:1200px)").matches
      ) {
        clearTimeout(timer);
        clearTimeout(menuTimers.get(menu));
        menu.classList.remove("menu-closing");
        closeMenus(menu);
        menu.open = true;
      }
    });
    menu.addEventListener("pointerleave", () => {
      timer = setTimeout(() => {
        if (!menu.contains(document.activeElement)) closeMenu(menu);
      }, 150);
    });
    menu.addEventListener("focusout", () =>
      setTimeout(() => {
        if (!menu.contains(document.activeElement)) closeMenu(menu);
      }, 0),
    );
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".nav-dropdown")) closeMenus();
  });

  // Preview panels activate on hover, click and vertical keyboard navigation.
  $$(".preview-menu").forEach((root) => {
    const tablist = $(".preview-tabs", root);
    const buttons = $$("[role=tab]", tablist);
    const panels = $$(":scope > [role=tabpanel]", root);
    function select(button) {
      buttons.forEach((tab) => {
        const active = tab === button;
        tab.setAttribute("aria-selected", String(active));
        tab.tabIndex = active ? 0 : -1;
      });
      panels.forEach(
        (panel) =>
          (panel.hidden = panel.id !== button.getAttribute("aria-controls")),
      );
    }
    buttons.forEach((button, index) => {
      button.addEventListener("pointerenter", (event) => {
        if (event.pointerType === "mouse") select(button);
      });
      button.addEventListener("click", () => select(button));
      button.addEventListener("keydown", (event) => {
        const key = event.key;
        let next;
        if (key === "ArrowDown") next = (index + 1) % buttons.length;
        if (key === "ArrowUp")
          next = (index - 1 + buttons.length) % buttons.length;
        if (key === "Home") next = 0;
        if (key === "End") next = buttons.length - 1;
        if (next !== undefined) {
          event.preventDefault();
          select(buttons[next]);
          buttons[next].focus();
        }
      });
    });
  });

  const menuButton = $(".menu-toggle");
  const mobileNav = $("#mobile-nav");
  const closeMobile = () => {
    mobileNav.hidden = true;
    document.body.classList.remove("mobile-menu-open");
    menuButton.setAttribute("aria-expanded", "false");
  };
  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") === "true";
    mobileNav.hidden = expanded;
    document.body.classList.toggle("mobile-menu-open", !expanded);
    menuButton.setAttribute("aria-expanded", String(!expanded));
  });
  matchMedia("(min-width:1200px)").addEventListener("change", (event) => {
    if (event.matches) closeMobile();
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".site-header")) closeMobile();
  });

  $(".mobile-menu-close").addEventListener("click", () => {
    closeMobile();
    menuButton.focus();
  });
  $$(".mobile-menu-groups > details").forEach((group) =>
    group.addEventListener("toggle", () => {
      if (group.open)
        $$(".mobile-menu-groups > details").forEach((other) => {
          if (other !== group) other.open = false;
        });
    }),
  );
  const dialog = $(".search-dialog");
  const search = $("#site-search");
  const results = $(".search-results");
  const empty = $(".search-empty");
  const searchIndex = $$(".search-index a");
  const mobileSearch = $(".mobile-search-input");
  const mobileSearchResults = $(".mobile-search-results");
  mobileSearch.addEventListener("input", () => {
    const query = mobileSearch.value
      .trim()
      .normalize("NFKC")
      .replaceAll("ي", "ی")
      .replaceAll("ك", "ک")
      .toLowerCase();
    const matches = searchIndex.filter((item) =>
      item.textContent
        .normalize("NFKC")
        .replaceAll("ي", "ی")
        .replaceAll("ك", "ک")
        .toLowerCase()
        .includes(query),
    );
    mobileSearchResults.replaceChildren(
      ...matches.map((item) => item.cloneNode(true)),
    );
    mobileSearchResults.hidden = !query;
  });
  function updateSearch() {
    const query = search.value
      .trim()
      .normalize("NFKC")
      .replaceAll("ي", "ی")
      .replaceAll("ك", "ک")
      .toLocaleLowerCase();
    const matches = searchIndex.filter((item) =>
      item.textContent
        .normalize("NFKC")
        .replaceAll("ي", "ی")
        .replaceAll("ك", "ک")
        .toLocaleLowerCase()
        .includes(query),
    );
    results.replaceChildren(...matches.map((item) => item.cloneNode(true)));
    empty.hidden = matches.length > 0;
  }
  $(".search-open").addEventListener("click", () => {
    closeMenus();
    dialog.showModal();
    updateSearch();
    search.focus();
  });
  $(".search-close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      const r = dialog.getBoundingClientRect();
      if (
        event.clientX < r.left ||
        event.clientX > r.right ||
        event.clientY < r.top ||
        event.clientY > r.bottom
      )
        dialog.close();
    }
  });
  search.addEventListener("input", updateSearch);

  const bubble = $(".contact-bubble");
  const drawer = $("#contact-drawer");
  const closeDrawer = () => {
    drawer.hidden = true;
    bubble.setAttribute("aria-expanded", "false");
  };
  bubble.addEventListener("click", () => {
    const expanded = bubble.getAttribute("aria-expanded") === "true";
    drawer.hidden = expanded;
    bubble.setAttribute("aria-expanded", String(!expanded));
    if (!expanded) $(".drawer-close").focus();
  });
  $(".drawer-close").addEventListener("click", () => {
    closeDrawer();
    bubble.focus();
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".contact-drawer,.contact-bubble")) closeDrawer();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      if (dialog.open) dialog.close();
      const activeMenu = dropdowns.find((menu) => menu.open);
      if (activeMenu) {
        closeMenus();
        $("summary", activeMenu).focus();
      }
      if (!mobileNav.hidden) {
        closeMobile();
        menuButton.focus();
      }
      if (!drawer.hidden) {
        closeDrawer();
        bubble.focus();
      }
    }
  });

  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries) =>
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            if (!reduced.matches) entry.target.classList.add("entered");
            revealObserver.unobserve(entry.target);
          }
        }),
      { threshold: 0.1 },
    );
    $$(".reveal").forEach((element) => revealObserver.observe(element));
    const serviceLinks = $$(".service-index a");
    const serviceObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible.length)
          serviceLinks.forEach((link) => {
            const active = link.hash === "#" + visible[0].target.id;
            link.classList.toggle("active", active);
            if (active) link.setAttribute("aria-current", "location");
            else link.removeAttribute("aria-current");
          });
      },
      { rootMargin: "-110px 0px -45% 0px", threshold: 0 },
    );
    $$(".service-card").forEach((element) => serviceObserver.observe(element));
  }

  const tabs = $$(".tech-tabs [role=tab]");
  const panels = $$(".technology [role=tabpanel]");
  function activateTab(tab) {
    tabs.forEach((item) => {
      const selected = item === tab;
      item.setAttribute("aria-selected", String(selected));
      item.tabIndex = selected ? 0 : -1;
    });
    panels.forEach((panel) => {
      panel.hidden = panel.id !== tab.getAttribute("aria-controls");
    });
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateTab(tab));
    tab.addEventListener("keydown", (event) => {
      let next;
      const rtl = document.documentElement.dir === "rtl";
      if (event.key === "ArrowDown") next = (index + 1) % tabs.length;
      if (event.key === "ArrowUp")
        next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "ArrowRight")
        next = (index + (rtl ? -1 : 1) + tabs.length) % tabs.length;
      if (event.key === "ArrowLeft")
        next = (index + (rtl ? 1 : -1) + tabs.length) % tabs.length;
      if (event.key === "Home") next = 0;
      if (event.key === "End") next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        activateTab(tabs[next]);
        tabs[next].focus();
      }
    });
  });
  $$(".faq").forEach((faq) =>
    faq.addEventListener("toggle", () => {
      if (faq.open)
        $$(".faq").forEach((other) => {
          if (other !== faq) other.open = false;
        });
    }),
  );

  $$(".reference-stars").forEach((root) => {
    for (let index = 0; index < 85; index++) {
      const star = document.createElement("i");
      star.style.left = ((index * 73.31 + 11) % 100) + "%";
      star.style.top = ((index * 37.73 + 3) % 100) + "%";
      star.style.animationDelay = -((index * 1.37) % 5) + "s";
      star.style.animationDuration = 3 + (index % 5) + "s";
      root.append(star);
    }
  });
  const marquee = $(".marquee-track");
  const animateElements = $$(".marquee-track,.reference-stars i,.flow-line");
  function animationVisibility() {
    animateElements.forEach((element) => {
      const r = element.getBoundingClientRect();
      element.style.animationPlayState =
        document.hidden || r.bottom < 0 || r.top > innerHeight ? "paused" : "";
    });
  }
  addEventListener("visibilitychange", animationVisibility);
  addEventListener("scroll", animationVisibility, { passive: true });
  if (marquee) {
    const sizeMarquee = () => {
      const group = $(".marquee-group", marquee);
      if (group)
        marquee.style.animationDuration =
          group.getBoundingClientRect().width / 50 + "s";
    };
    document.fonts.ready.then(sizeMarquee);
    addEventListener("resize", sizeMarquee, { passive: true });
  }
  animationVisibility();

  const form = $("#project-form");
  if (form) {
    const service = $("#service");
    const preferred = new URLSearchParams(location.search).get("service");
    if ([...service.options].some((option) => option.value === preferred))
      service.value = preferred;
    const draft = $(".draft-text");
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const name = $("#name").value.trim();
      const email = $("#email").value.trim();
      const brief = $("#brief").value.trim();
      if (!name || brief.length < 20) {
        $("#brief").setCustomValidity(
          document.documentElement.lang === "fa"
            ? "لطفاً دست‌کم ۲۰ نویسه درباره پروژه بنویسید."
            : "Please enter at least 20 characters about your project.",
        );
        $("#brief").reportValidity();
        return;
      }
      const serviceName = service.value
        ? service.selectedOptions[0].textContent
        : "";
      const subject =
        "Binux project inquiry" + (serviceName ? ": " + serviceName : "");
      draft.value = `${name}\n${email}\n${serviceName}\n\n${brief}`;
      $(".draft-result").hidden = false;
      location.href = `mailto:alireza.4mini@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(draft.value)}`;
    });
    $("#brief").addEventListener("input", () =>
      $("#brief").setCustomValidity(""),
    );
    $(".copy-draft").addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(draft.value);
        $(".copy-status").textContent = form.dataset.copied;
      } catch {
        draft.focus();
        draft.select();
        $(".copy-status").textContent = form.dataset.copyError;
      }
    });
  }
})();
