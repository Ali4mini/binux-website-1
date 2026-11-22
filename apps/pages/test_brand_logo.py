from pathlib import Path
from typing import cast

from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase

from .views import _organization_schema, _seo_image_url


class SuppliedBrandLogoTests(SimpleTestCase):
    def test_uploaded_logo_is_shared_by_header_footer_and_mobile_in_both_languages(self):
        for lang in ("fa", "en"):
            with self.subTest(lang=lang):
                response = cast(HttpResponse, self.client.get(f"/{lang}/"))
                html = response.content.decode()
                header = html.split("<header", 1)[1].split("</header>", 1)[0]
                footer = html.split("<footer", 1)[1].split("</footer>", 1)[0]
                self.assertGreaterEqual(header.count('class="brand-mark"'), 2)
                self.assertIn('class="brand-mark"', footer)
                self.assertIn('/static/website/favicon.png', html)
                self.assertIn('property="og:image" content="https://binux.tech/static/images/logo.png"', html)
                self.assertIn('name="twitter:image" content="https://binux.tech/static/images/logo.png"', html)
                self.assertNotIn('/static/website/favicon.svg', html)
                self.assertNotIn('aria-hidden="true">B<span', footer)

    def test_shared_css_points_to_same_uploaded_image_in_light_and_dark(self):
        css = Path(cast(str, finders.find("website/reference.css"))).read_text()
        self.assertIn('../images/logo.png', css)
        self.assertNotIn('../images/logo-light.svg', css)
        self.assertNotIn('../images/logo-dark.svg', css)
        for filename in ("images/logo.png", "website/favicon.png"):
            path = Path(cast(str, finders.find(filename)))
            self.assertTrue(path.is_file())
            self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")

    def test_legacy_logo_and_metadata_use_same_asset(self):
        request = RequestFactory().get("/fa/")
        self.assertTrue(str(_seo_image_url(request)).endswith("/static/images/logo.png"))
        self.assertEqual(_organization_schema(request)["logo"]["url"], _seo_image_url(request))
        template = Path(__file__).resolve().parents[2] / "templates/pages/home.html"
        self.assertIn("{% static 'images/logo.png' %}", template.read_text())
