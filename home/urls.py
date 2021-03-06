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
from home.views import *

urlpatterns = [
    url(r'^$', login_required(home, login_url='/home/home_login/'), name='home'),

    url(r'^home_login/$', home_login, name='home_login'),

    url(r'^home_logon/$', home_logon, name='home_logon'),

    url(r'^home_logout/$', home_logout, name='home_logout'),


]
