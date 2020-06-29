
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultation/', views.consultation, name='consultation'),
    path('add_consultation/', views.add_consultation, name='add_consultation'),
    path('about/', views.contact, name='contact'),
    path('contact/', views.contacts, name='contacts'),
    path('credit-calculator/', views.credit_calculator, name='credit_calculator'),
    path('credit-help/', views.credit_help, name='credit_help'),
    path('jobs/', views.jobs, name='jobs'),
    path('owners/', views.owners, name='owners'),
    path('partners/', views.partners, name='partners'),
    path('privatization/', views.privatization, name='privatization'),

    path('robots.txt', views.robots, name='robots'),

]
