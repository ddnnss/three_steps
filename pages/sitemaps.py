from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from ads.models import Ads
from article.models import Article



class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return ['index','contact','contacts','consultation','credit_calculator','credit_help',
                'jobs','owners','partners','privatization','sell','estimate']

    def location(self, item):
        return reverse(item)



class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Article.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.created_at

class AdsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Ads.objects.filter(is_publish=True)

    def lastmod(self, obj):
        return obj.created_at