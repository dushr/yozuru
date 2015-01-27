from django.contrib.syndication.views import Feed
from api.models import Entry


class LatestPosts(Feed):
    title = "Yozuru CMS"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]