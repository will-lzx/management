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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from home.views import home_login, agreement
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', include('home.urls')),
    url(r'^hardware/', include('hardware.urls')),
    url(r'^customer/', include('customer.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^analysis/', include('analysis.urls')),
    # url(r'^accounts/login/$', home_login, name='home_login'),
    url(r'^login/agreement/$', agreement, name='agreement'),
]
