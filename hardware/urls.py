"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from hardware.views import *

urlpatterns = [
    url(r'^$', hardware, name='hardware'),

    # cabinet
    url(r'^cabinet/$', cabinet, name='cabinet'),
    url(r'^cabinet/cabinet_add/$', cabinet_add, name='cabinet_add'),
    url(r'^cabinet/cabinet_delete/$', cabinet_delete, name='cabinet_delete'),
    url(r'^cabinet/cabinet_update/(?P<cabinet_id>.+)/$', cabinet_update, name='cabinet_update'),
    url(r'^cabinet/cabinet_update_submit/$', cabinet_update_submit, name='cabinet_update_submit'),

    # pole
    url(r'^pole/$', pole, name='pole'),
    url(r'^pole/pole_add/$', pole_add, name='pole_add'),
    url(r'^pole/pole_delete/$', pole_delete, name='pole_delete'),
    url(r'^pole/pole_update/(?P<pole_id>.+)/$', pole_update, name='pole_update'),
    url(r'^pole/pole_update_submit/$', pole_update_submit, name='pole_update_submit'),

    # spot
    url(r'^spot/$', spot, name='spot'),
    url(r'^spot/spot_add/$', spot_add, name='spot_add'),
    url(r'^spot/spot_delete/$', spot_delete, name='spot_delete'),
    url(r'^spot/spot_update/(?P<spot_id>.+)/$', spot_update, name='spot_update'),
    url(r'^spot/spot_update_submit/$', spot_update_submit, name='spot_update_submit'),
]
