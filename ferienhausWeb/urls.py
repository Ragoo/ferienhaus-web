from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ferienhaus_beschreibung/$', views.ferienhaus, name='ferienhaus'),
    url(r'^ferienhaus_galerie/$', views.ferienhaus_galerie, name='ferienhaus_galerie'),
    url(r'^belegungskalender/$', views.belegungskalender, name='belegungskalender'),
    url(r'^umgebung/$', views.umgebung, name='umgebung'),
    url(r'^umgebung/(?P<pk>\d+)/$', views.trip_detail, name='trip_detail'),
    url(r'^gaestebuch/$', views.guestbook,name='guestbook'),
    #Forms
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]