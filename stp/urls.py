# -*- coding: utf-8 -*-
# En este archivo se definen las URL que llevan a cada una de las vistas
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^mobibus/$', views.MobibusList.as_view()),
    url(r'^mobibus/(?P<pk>\w+)/$', views.MobibusDetail.as_view()),
    url(r'^gps/$', views.GPSList.as_view()),
    url(r'^gps/(?P<pk>\w+)/$', views.GPSDetail.as_view()),
    url(r'^gps/(?P<gps_pk>\w+)/eventos/$', views.EventoList.as_view()),
    url(r'^vcub/$', views.VCubList.as_view()),
    url(r'^vcub/(?P<pk>\d+)/$', views.VCubDetail.as_view()),
    url(r'^estacionvcub/$', views.EstacionVCubList.as_view()),
    url(r'^estacionvcub/(?P<pk>\d+)/$', views.EstacionVCubDetail.as_view()),
    url(r'^estacionvcub/(?P<pk>\d+)/alquilarvcub/(?P<pkvcub>\d+)?$', views.AlquilarVCub.as_view()),
    #url(r'^gps/(?P<gpspk>\w+)/eventos/(?P<pk>\w+)/$', views.GPSDetail.as_view()),
]
