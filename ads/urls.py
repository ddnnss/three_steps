from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('feed/feed.xml', views.feed, name='feed'),
    path('<ads_number>', views.show_ads, name='show_ads'),




]