from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_safe
from .content import CONTENT, SERVICES, PROJECTS, ARTICLES
from .navigation import navigation


@require_safe
def localized(request, lang, page='home', slug=None):
    if lang not in CONTENT:
        raise Http404
    c = CONTENT[lang]
    services = [dict(s, **s[lang]) for s in SERVICES]
    projects = [dict(p, **p[lang]) for p in PROJECTS]
    articles = [dict(a, **a[lang]) for a in ARTICLES]
    detail = None
    if slug:
        collection = {'service': services, 'project': projects, 'article': articles}.get(page, [])
        detail = next((s for s in collection if s['slug'] == slug), None)
        if detail is None:
            raise Http404
    other = 'en' if lang == 'fa' else 'fa'
    route_args = {'lang': other}
    if slug:
        route_args['slug'] = slug
    language_url = reverse('website:' + page, kwargs=route_args)
    title = detail['title'] if detail else c['titles'][page]
    context = {'lang': lang, 'c': c, 'services': services, 'projects': projects,
               'articles': articles, 'detail': detail, 'page': page,
               'language_url': language_url, 'title': title,
               'canonical': 'https://binux.tech' + request.path,
               'alternate_en': request.path.replace('/fa/', '/en/', 1),
               'alternate_fa': request.path.replace('/en/', '/fa/', 1)}
    context.update(navigation(lang))
    return render(request, 'website/page.html', context)


def legacy(request, destination='home'):
    return redirect('website:' + destination, lang='fa', permanent=True)


def sitemap(request):
    paths = []
    for lang in CONTENT:
        for page in ['home', 'services', 'work', 'about', 'process', 'contact', 'insights', 'privacy']:
            paths.append(reverse('website:' + page, kwargs={'lang': lang}))
        for page, collection in [('service', SERVICES), ('project', PROJECTS), ('article', ARTICLES)]:
            paths += [reverse('website:' + page, kwargs={'lang': lang, 'slug': item['slug']}) for item in collection]
    xml = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    xml += ''.join(f'<url><loc>https://binux.tech{path}</loc></url>' for path in paths)
    return HttpResponse(xml + '</urlset>', content_type='application/xml')
