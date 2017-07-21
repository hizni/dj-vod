
from django.conf.urls import include, url
from django.contrib import admin
from vod_webapp import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.landing, name='index'),
]
