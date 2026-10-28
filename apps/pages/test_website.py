from xml.etree import ElementTree
from django.test import SimpleTestCase, override_settings
from django.urls import reverse
from .content import CONTENT, SERVICES, PROJECTS, ARTICLES


@override_settings(ALLOWED_HOSTS=['testserver'])
class BilingualWebsiteTests(SimpleTestCase):
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
        self.assertContains(response, 'mailto:alireza.4mini@gmail.com')
        self.assertEqual(self.client.post('/en/contact/', {'brief': 'Do not store this'}).status_code, 405)
