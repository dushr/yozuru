from django.contrib.sitemaps import GenericSitemap
from api.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'blog': GenericSitemap(info_dict, priority=0.6),
}