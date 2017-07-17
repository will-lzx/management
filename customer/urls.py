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

from customer.views import *

urlpatterns = [
    url(r'^$', login_required(customer, login_url='/home/home_login/'), name='customer'),
    url(r'^lendhistory/(?P<mobile_number>.+)/$', login_required(lendhistory, login_url='/home/home_login/'), name='lendhistory'),

    url(r'^search/$', login_required(search, login_url='/home/home_login/'), name='search'),

    url(r'^lendmanagement/$', login_required(lendmanagement, login_url='/home/home_login/'), name='lendmanagement'),

    # rule
    url(r'^rule/$', login_required(rule, login_url='/home/home_login/'), name='rule'),
    url(r'^rule/rule_add/$', login_required(rule_add, login_url='/home/home_login/'), name='rule_add'),
    url(r'^rule/rule_delete/$', login_required(rule_delete, login_url='/home/home_login/'), name='rule_delete'),
    url(r'^rule/rule_update/(?P<rule_id>.+)/$', login_required(rule_update, login_url='/home/home_login/'), name='rule_update'),
    url(r'^rule/rule_update_submit/$', login_required(rule_update_submit, login_url='/home/home_login/'), name='rule_update_submit'),

]
