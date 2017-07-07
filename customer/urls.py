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
from customer.views import *

urlpatterns = [
    url(r'^$', customer, name='customer'),

    # rule
    url(r'^rule/$', rule, name='rule'),
    url(r'^rule/rule_add/$', rule_add, name='rule_add'),
    url(r'^rule/rule_delete/$', rule_delete, name='rule_delete'),
    url(r'^rule/rule_update/(?P<rule_id>.+)/$', rule_update, name='rule_update'),
    url(r'^rule/rule_update_submit/$', rule_update_submit, name='rule_update_submit'),

]
