from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('feed/living_feed.xml', views.living_feed, name='living_feed'),
    path('feed/comm_feed.xml', views.comm_feed, name='comm_feed'),
    path('<ads_number>', views.show_ads, name='show_ads'),




]