from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ferienhaus_beschreibung/$', views.ferienhaus, name='ferienhaus'),
    url(r'^ferienhaus_galerie/$', views.ferienhaus_galerie, name='ferienhaus_galerie'),
    url(r'^belegungskalender/$', views.belegungskalender, name='belegungskalender'),
    url(r'^umgebung/$', views.umgebung, name='umgebung'),
    url(r'^umgebung/(?P<pk>\d+)/$', views.trip_detail, name='trip_detail'),
    url(r'^gaestebuch/$', views.guestbook, name='guestbook'),
    # Forms
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

    url(r'^trip/new/$', views.trip_new, name='trip_new'),
    url(r'^trip/(?P<pk>\d+)/edit/$', views.trip_edit, name='trip_edit'),
    url(r'^trip/(?P<pk>\d+)/remove/$', views.trip_remove, name='trip_remove'),

    url(r'^guestbook/(?P<pk>\d+)/remove/$', views.guestbook_remove, name='guestbook_remove'),

    url(r'^galeryimage/new/$', views.galeryimage_new, name='galeryimage_new'),
    url(r'^galeryimage/(?P<pk>\d+)/remove/$', views.galeryimage_remove, name='galeryimage_remove'),
]
