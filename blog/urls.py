from django.conf.urls import patterns, include, url
import views
import feed

urlpatterns = patterns(
    '',
    url('^$', views.BlogIndex.as_view(), name='index'),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
)