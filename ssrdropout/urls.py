"""webguild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from rest_framework import routers
from rest_framework import views

from .views import IndexView

from guildmember.views import guildmember_api

router = routers.SimpleRouter()
router.register(r'members', guildmember_api.MemberViewSet)
router.register(r'pools', guildmember_api.PoolViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/api-view/', include('guildmember.urls', namespace='api-view-v1')),
    url(r'^api/v2/', include(router.urls, namespace='api-view-v2')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^members/', include('guildmember.urls')),
]
