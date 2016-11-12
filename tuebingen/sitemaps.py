from django.contrib.sitemaps import Sitemap
from top_page.models import Whatsnew, Upcoming
from giveinfo.models import Experience, Experiencetext, Article, Articletext, Link, Summary


class TopSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Whatsnew.objects.filter(is_draft=False), Upcoming.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date

class TestSitemap(Sitemap):

    def items(self):
        return Test.objects.all()[:2]

    def lastmod(self, obj):
        return obj.update_date

    def location(self, obj):
        return "/News/" + str(obj.id) + "/"

    def priority(self, obj):
        return 0.5

    def changefreq(self, obj):
        return "weekly"
