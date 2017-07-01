from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'pages/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'pages/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
