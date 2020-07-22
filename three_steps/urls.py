from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
# from pages.views import customhandler404
from django.views.generic.base import RedirectView
from pages.sitemaps import *
from django.contrib.sitemaps.views import sitemap

admin.site.site_header = "3 ступени"
admin.site.site_title =  "3 ступени администрирование"
admin.site.index_title = "3 ступени администрирование"

sitemaps = {
     'static': StaticViewSitemap,
    'ads' : AdsSitemap,
    'articles': ArticleSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cp/', include('cp.urls')),
    path('user/', include('customuser.urls')),
    path('ads/', include('ads.urls')),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    path('articles/', include('article.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = customhandler404