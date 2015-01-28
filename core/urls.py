from django.conf.urls import patterns, include, url
from django.conf.urls import handler404, handler500

from django.contrib import admin
import static_pages.views as page
from blog.sitemap import sitemaps

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'yozuru.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # core views
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'auth_app.views.user_login', name='login'),
    url(r'^logout/', 'auth_app.views.user_logout', name='logout'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # external apps
    url(r'^markdown/', include('django_markdown.urls')),

    # yozuru apps views
    url(r'^', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),

    url(r'^about/', page.About.as_view(), name='about'),
)


handler404 = 'blog.views.error404'
handler500 = 'blog.views.error500'