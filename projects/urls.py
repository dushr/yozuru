from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url('^$', views.ProjectIndex.as_view(), name='project_index'),
    url(r'^(?P<slug>\S+)$', views.ProjectDetail.as_view(), name="project_detail"),
)