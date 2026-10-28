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
    header.classList.toggle("scrolled", scrollY > 150);
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
  const closeMenus = (except) =>
    dropdowns.forEach((menu) => {
      if (menu !== except) menu.open = false;
    });
  dropdowns.forEach((menu) => {
    let timer;
    menu.addEventListener("toggle", () => {
      if (menu.open) closeMenus(menu);
    });
    menu.addEventListener("pointerenter", (event) => {
      if (
        event.pointerType === "mouse" &&
        matchMedia("(min-width:1051px)").matches
      ) {
        clearTimeout(timer);
        closeMenus(menu);
        menu.open = true;
      }
    });
    menu.addEventListener("pointerleave", () => {
      timer = setTimeout(() => {
        if (!menu.contains(document.activeElement)) menu.open = false;
      }, 150);
    });
    menu.addEventListener("focusout", () =>
      setTimeout(() => {
        if (!menu.contains(document.activeElement)) menu.open = false;
      }, 0),
    );
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".nav-dropdown")) closeMenus();
  });

  const menuButton = $(".menu-toggle");
  const mobileNav = $("#mobile-nav");
  const closeMobile = () => {
    mobileNav.hidden = true;
    menuButton.setAttribute("aria-expanded", "false");
  };
  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") === "true";
    mobileNav.hidden = expanded;
    menuButton.setAttribute("aria-expanded", String(!expanded));
  });
  matchMedia("(min-width:1051px)").addEventListener("change", (event) => {
    if (event.matches) closeMobile();
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".site-header")) closeMobile();
  });

  const dialog = $(".search-dialog");
  const search = $("#site-search");
  const results = $(".search-results");
  const empty = $(".search-empty");
  const searchIndex = $$(".search-index a");
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
