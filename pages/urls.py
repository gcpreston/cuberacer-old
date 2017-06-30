from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', login, {'template_name': 'timer/login.html'}),
    url(r'^logout/$', views.logout_user),
]
