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
from django.contrib.auth.decorators import login_required

from hardware.views import *

urlpatterns = [
    url(r'^$', login_required(hardware, login_url='/home/home_login/'), name='hardware'),

    # cabinet
    url(r'^cabinet/$', login_required(cabinet, login_url='/home/home_login/'), name='cabinet'),
    url(r'^cabinet/cabinet_add/$', login_required(cabinet_add, login_url='/home/home_login/'), name='cabinet_add'),
    url(r'^cabinet/cabinet_delete/$', login_required(cabinet_delete, login_url='/home/home_login/'), name='cabinet_delete'),
    url(r'^cabinet/cabinet_update/(?P<cabinet_id>.+)/$', login_required(cabinet_update, login_url='/home/home_login/'), name='cabinet_update'),
    url(r'^cabinet/cabinet_update_submit/$', login_required(cabinet_update_submit, login_url='/home/home_login/'), name='cabinet_update_submit'),

    # pole
    url(r'^pole/$', login_required(pole, login_url='/home/home_login/'), name='pole'),
    url(r'^pole/pole_add/$', login_required(pole_add, login_url='/home/home_login/'), name='pole_add'),
    url(r'^pole/pole_delete/$', login_required(pole_delete, login_url='/home/home_login/'), name='pole_delete'),
    url(r'^pole/pole_update/(?P<pole_id>.+)/$', login_required(pole_update, login_url='/home/home_login/'), name='pole_update'),
    url(r'^pole/pole_update_submit/$', login_required(pole_update_submit, login_url='/home/home_login/'), name='pole_update_submit'),

    # spot
    url(r'^spot/$', login_required(spot, login_url='/home/home_login/'), name='spot'),
    url(r'^spot/spot_add/$', login_required(spot_add, login_url='/home/home_login/'), name='spot_add'),
    url(r'^spot/spot_delete/$', spot_delete, name='spot_delete'),
    url(r'^spot/spot_update/(?P<spot_id>.+)/$', spot_update, name='spot_update'),
    url(r'^spot/spot_update_submit/$', spot_update_submit, name='spot_update_submit'),
]
