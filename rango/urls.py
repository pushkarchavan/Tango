from django.conf.urls import patterns, url
from rango import views

#Rango URLS
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
)