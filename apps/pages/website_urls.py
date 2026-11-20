from django.http import HttpResponse
from django.urls import path, register_converter
from . import website_views as views

class LanguageConverter:
    regex = 'en|fa'
    def to_python(self, value): return value
    def to_url(self, value): return value

register_converter(LanguageConverter, 'language')
app_name = 'website'
urlpatterns = [
    path('', views.legacy, name='root'),
    path('about/', views.legacy, {'destination': 'about'}),
    path('articles/', views.legacy, {'destination': 'insights'}),
    path('electronics/', views.legacy, {'destination': 'services'}),
    path('sitemap.xml', views.sitemap),
    path('robots.txt', lambda request: HttpResponse('User-agent: *\nAllow: /\nSitemap: https://binux.tech/sitemap.xml\n', content_type='text/plain')),
    path('<language:lang>/', views.localized, name='home'),
]
for name, route in [('services', 'services/'), ('work', 'work/'), ('about', 'company/'),
                    ('process', 'how-we-work/'), ('contact', 'contact/'),
                    ('insights', 'insights/'), ('privacy', 'privacy/')]:
    urlpatterns.append(path('<language:lang>/' + route, views.localized, {'page': name}, name=name))
for name, route in [('service', 'services'), ('project', 'work'), ('article', 'insights')]:
    urlpatterns.append(path(f'<language:lang>/{route}/<slug:slug>/', views.localized, {'page': name}, name=name))
