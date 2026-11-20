from xml.etree import ElementTree
import re
from typing import cast
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase, override_settings
from django.urls import reverse
from .content import CONTENT, SERVICES, PROJECTS, ARTICLES


@override_settings(ALLOWED_HOSTS=['testserver'])
class BilingualWebsiteTests(SimpleTestCase):
    def test_header_keeps_phone_and_language_switcher_without_topbar_label(self):
        for lang in ('fa', 'en'):
            with self.subTest(lang=lang):
                html = cast(HttpResponse, self.client.get(f'/{lang}/')).content.decode()
                topbar = re.search(r'<div class="topbar container">(.*?)</div>', html, re.S)
                assert topbar is not None
                self.assertIn('class="topbar-phone"', topbar.group(1))
                self.assertNotIn('فارسی و انگلیسی', topbar.group(1))
                self.assertNotIn('Persian & English', topbar.group(1))
                self.assertIn('class="language"', html)

    def test_work_dropdown_links_to_every_project_without_preview_panels(self):
        for lang in ('fa', 'en'):
            with self.subTest(lang=lang):
                html = cast(HttpResponse, self.client.get(f'/{lang}/')).content.decode()
                work = re.search(r'<div class="mega-menu work-[^>]*>(.*?)</div></details>', html, re.S)
                assert work is not None
                work_html = work.group(1)
                self.assertNotIn('preview-content', work_html)
                self.assertNotIn('preview-proof', work_html)
                self.assertNotIn('role="tab"', work_html)
                self.assertNotIn('role="tabpanel"', work_html)
                for project in PROJECTS:
                    href = reverse('website:project', kwargs={'lang': lang, 'slug': project['slug']})
                    self.assertIn(f'href="{href}"', work_html)
                self.assertIn('class="preview-tabs" role="tablist"', html)  # Services still uses tabs.

    def test_home_omits_process_band_but_process_page_keeps_steps(self):
        for lang in ('fa', 'en'):
            with self.subTest(lang=lang):
                home = cast(HttpResponse, self.client.get(f'/{lang}/')).content.decode()
                process_url = reverse('website:process', kwargs={'lang': lang})
                process = cast(HttpResponse, self.client.get(process_url)).content.decode()
                self.assertNotIn('class="process-section section"', home)
                self.assertNotIn('class="process-grid"', home)
                self.assertIn('class="process-grid"', process)

    def test_social_destinations_are_in_shared_footer_with_local_icons(self):
        for lang in ('fa', 'en'):
            for page in ('', 'company/'):
                with self.subTest(lang=lang, page=page):
                    html = cast(HttpResponse, self.client.get(f'/{lang}/{page}')).content.decode()
                    main, footer = html.split('</main>', 1)
                    self.assertNotIn('class="related-services"><a href="https://instagram.com/', main)
                    social = footer.split('class="footer-social"', 1)[1]
                    self.assertEqual(social.split('class="footer-bottom"', 1)[0].count('class="footer-social-icon"'), 4)
                    for icon in ('instagram', 'reddit', 'x', 'linkedin'):
                        self.assertIn(f'/static/website/social/{icon}.svg', social)
                        self.assertIsNotNone(finders.find(f'website/social/{icon}.svg'))

    def test_contact_buttons_dial_the_phone_shown_in_the_topbar(self):
        for lang in ('fa', 'en'):
            with self.subTest(lang=lang):
                html = cast(HttpResponse, self.client.get(f'/{lang}/')).content.decode()
                phone = re.search(r'class="topbar-phone" href="(tel:[^"]+)"', html)
                assert phone is not None
                href = phone.group(1)
                for selector in ('button nav-contact', 'button primary mobile-contact-action'):
                    button = re.search(r'class="' + selector + r'" href="([^"]+)"', html)
                    assert button is not None
                    self.assertEqual(button.group(1), href)
                quick_contact = re.search(r'class="mobile-quick-contact".*?href="mailto:[^"]+".*?<a class="button" href="([^"]+)"', html, re.S)
                assert quick_contact is not None
                self.assertEqual(quick_contact.group(1), href)

    def test_every_bilingual_page_and_equivalent_language_link(self):
        for lang in CONTENT:
            other = 'fa' if lang == 'en' else 'en'
            pages = [(p, None) for p in ['home', 'services', 'work', 'about', 'process', 'contact', 'insights', 'privacy']]
            for kind, collection in [('service', SERVICES), ('project', PROJECTS), ('article', ARTICLES)]:
                pages += [(kind, item['slug']) for item in collection]
            for kind, slug in pages:
                with self.subTest(lang=lang, page=kind, slug=slug):
                    kwargs = {'lang': lang}
                    if slug:
                        kwargs['slug'] = slug
                    url = reverse('website:' + kind, kwargs=kwargs)
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)
                    self.assertContains(response, f'lang="{lang}"')
                    self.assertContains(response, 'dir="rtl"' if lang == 'fa' else 'dir="ltr"')
                    self.assertContains(response, 'https://binux.tech' + url)
                    kwargs['lang'] = other
                    self.assertContains(response, f'href="{reverse("website:" + kind, kwargs=kwargs)}"')
                    self.assertNotContains(response, 'SolGuruz')
                    self.assertNotContains(response, '09120000000')

    def test_invalid_language_and_slug_return_404(self):
        for path in ['/de/', '/fa/services/unknown/', '/en/work/unknown/', '/fa/insights/unknown/']:
            self.assertEqual(self.client.get(path).status_code, 404)

    def test_sitemap_is_valid_and_contains_all_new_routes(self):
        response = self.client.get('/sitemap.xml')
        root = ElementTree.fromstring(response.content)
        locations = [node.text for node in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        self.assertEqual(len(locations), 38)
        self.assertEqual(len(locations), len(set(locations)))
        for location in locations:
            self.assertEqual(self.client.get(location.removeprefix('https://binux.tech')).status_code, 200)

    def test_root_and_legacy_entry_redirects(self):
        for path, destination in [('/', '/fa/'), ('/about/', '/fa/company/'), ('/articles/', '/fa/insights/')]:
            self.assertRedirects(self.client.get(path), destination, status_code=301)

    def test_email_form_explains_delivery_and_posts_are_not_accepted(self):
        response = self.client.get('/en/contact/')
        self.assertContains(response, 'Your message is sent only when you send that email.')
        self.assertContains(response, 'mailto:binuxtech.co@gmail.com')
        self.assertEqual(self.client.post('/en/contact/', {'brief': 'Do not store this'}).status_code, 405)

    def test_brand_film_is_second_section_and_reduced_motion_has_poster(self):
        response = self.client.get('/fa/')
        html = response.content.decode()
        hero = html.index('class="hero container"')
        film = html.index('class="brand-film"')
        marquee = html.index('class="work-marquee"')
        self.assertLess(hero, film)
        self.assertLess(film, marquee)
        film_markup = html[film:marquee]
        self.assertIn('binux-hero.mp4', film_markup)
        self.assertIn('binux-hero-poster.svg', film_markup)
        self.assertNotIn('autoplay', film_markup)

    def test_header_contact_theme_and_about_brand_profiles(self):
        home = self.client.get('/fa/')
        self.assertContains(home, 'tel:+982191013254')
        self.assertContains(home, 'class="theme-toggle"')
        home_context = home.context[0] if home.context else {}
        self.assertNotIn('nav_quote', home_context)
        self.assertNotIn('nav_ai', home_context)
        self.assertNotIn('nav_industries', home_context)

        about = self.client.get('/fa/company/')
        self.assertContains(about, 'binux.tech')
        self.assertContains(about, 'binux-tech')
        self.assertContains(about, 'binux_tech')
        self.assertNotContains(about, 'علیرضا امینی')
        self.assertNotContains(about, 'امیرعلی قاسمی')


from django.test import TestCase
class ErpScreenshotTests(TestCase):
    def test_meshcat_erp_uses_approved_local_screenshots_not_old_demo_media(self):
        from django.test import Client
        client = Client()
        response = client.get('/fa/work/meshcat-erp/')
        html = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('erp-screenshots/dashboard.png', html)
        self.assertIn('erp-screenshots/dashboard.png', html)
        self.assertNotIn('meshcat-dashboard-demo.png', html)
        self.assertNotIn('meshcat-erp-light.mp4', html)
        self.assertNotIn('reporting_dashboard.png', html)
        self.assertNotIn('sales_customers.png', html)
