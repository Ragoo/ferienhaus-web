from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ferienhaus_beschreibung/$', views.ferienhaus, name='ferienhaus'),
    url(r'^ferienhaus_galerie/$', views.ferienhaus_galerie, name='ferienhaus_galerie'),
    url(r'^belegugnskalender/$', views.belegugnskalender, name='belegugnskalender'),
]