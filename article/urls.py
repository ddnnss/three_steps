from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.articles, name='articles'),
    path('<article_name_slug>', views.article, name='article'),
   


]