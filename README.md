# Binux bilingual website

Full English and Persian business website built on the existing Django application. New content is server-rendered at `/en/` and `/fa/`; `/` redirects to Persian. There are 19 pages per language: homepage, services index, six service details, work index, three project details, company, process, contact, insights index, two guides and privacy.

## Run locally

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python manage.py runserver 127.0.0.1:8097 --settings=core.settings.preview
```

The preview settings use a temporary SQLite path and localhost only. New marketing pages need no database queries or migrations. The existing project admin, models, migrations, legacy service pages, uploaded media and article details remain in the application. Preview database migrations are needed only to exercise those older database features. Use the established production environment for deployment; never use the preview settings publicly.

## Check

```sh
.venv/bin/python manage.py check --settings=core.settings.preview
.venv/bin/python manage.py test apps.pages.test_website --settings=core.settings.preview
node --check static/website/site.js
git diff --check
```

Five test methods cover all 38 localized routes, route-preserving language switching, canonical URLs, sitemap coverage, invalid routes, entry redirects and contact delivery semantics. Browser QA covers desktop/mobile in both languages, menus, search, tabs, FAQ, form validation and email draft generation. Screenshots and local reports are in the ignored `.impeccable/review/` directory. Automated browser checks are local validation, not remote CI or production verification.

## Editing

- Public copy and translations: `apps/pages/content.py`.
- Localized routing/rendering: `apps/pages/website_urls.py`, `website_views.py`.
- Templates: `templates/website/`.
- CSS and interactions: `static/website/site.css`, `site.js`.
- Design tokens and direction: `DESIGN.md`, `.impeccable/design.json`, `.impeccable/surfaces/website.md`.
- Provenance and publishing boundaries: `ASSETS.md`.

Locale is carried by the URL rather than a browser-only translation layer. Canonicals and English/Persian hreflang links are server-rendered. Native `<details>` menus and FAQs remain usable without JavaScript. Search runs locally and sends no query to a third party. Motion respects reduced-motion preferences.

## Reference and scope

The visual reference is https://solguruz.com/, inspected on 2026-10-28. This is an independently implemented Binux adaptation: white layout, large geometric typography, outlined floating/sticky navigation, blue shadowed actions, pastel capability pills, marquee, dark statement section, alternating project cards, sticky service index, process, technology tabs, FAQ, contact drawer and footer.

It is **not verified pixel-identical**. Display typography uses open-license Manrope in place of the reference's Panamera. Binux copy, team, portfolio and language controls replace the reference's company content. SolGuruz testimonials, client logos, ratings, awards, certifications, videos, calculators and third-party tracking are not included. Existing unlocalized article and service-detail URLs retain their earlier content/templates for compatibility; the new navigation leads exclusively to bilingual pages. This build does not claim to translate every legacy article or reproduce the reference's entire catalog of industry landing pages.

The contact form **prepares a mailto draft**, not a server-sent message. It validates required fields, preselects the requested service, exposes the composed text and offers clipboard fallback. No submission database, SMTP delivery or false success message is present. Configure a real delivery backend separately if server-side submission is required.

## Deployment state

Source branch: `feat/bilingual-solguruz`, based on production commit `bf3da81` in `Ali4mini/binux-website-1`. Original checkout `/home/dev/binux web` was left untouched. Production replacement is not part of the preview deployment. Hosting/deployment belongs to Hermes; the confirmed preview URL and exact deployed source identity must be recorded in the handoff.
