from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [

    path('<ads_number>', views.show_ads, name='show_ads'),
   


]