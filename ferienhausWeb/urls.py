from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ferienhaus_beschreibung/$', views.ferienhaus, name='ferienhaus'),
    url(r'^ferienhaus_galerie/$', views.ferienhaus_galerie, name='ferienhaus_galerie'),
    url(r'^preise/$', views.preise, name='preise'),
    url(r'^umgebung/$', views.umgebung, name='umgebung'),
    url(r'^umgebung/(?P<pk>\d+)/$', views.trip_detail, name='trip_detail'),
    url(r'^gaestebuch/$', views.guestbook, name='guestbook'),

    url(r'^marker_list/$', views.marker_list, name='marker_list'),
    url(r'^markericon_list/$', views.markericon_list, name='markericon_list'),
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

    url(r'^marker/(?P<pk>\d+)/edit/$', views.marker_edit, name='marker_edit'),
    url(r'^marker/(?P<pk>\d+)/remove/$', views.marker_remove, name='marker_remove'),

    url(r'^markericon/(?P<pk>\d+)/edit/$', views.markericon_edit, name='markericon_edit'),
    url(r'^markericon/(?P<pk>\d+)/remove/$', views.markericon_remove, name='markericon_remove'),

    url(r'^belegungskalender/$', TemplateView.as_view(template_name='ferienhausWeb/belegungskalender.html'),
        name='belegungskalender'),
    url(r'^eventsXML/$', views.eventsXML, name='eventsXML'),
    url(r'^dataprocessor/$', views.dataprocessor, name='dataprocessor'),

    url(r'^text/(?P<pk>\d+)/edit/$', views.text_edit, name='text_edit'),
]
