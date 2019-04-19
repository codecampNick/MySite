from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='employment_home'),
    url(r'dice-holdings-inc/?', views.diceholdings, name='aboutDiceHoldings'),
    url(r'health-ecareers/?$', views.healthecareers, name='aboutHealthecareers'),
]