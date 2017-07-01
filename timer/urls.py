from django.conf.urls import url

from . import views

app_name = 'timer'
urlpatterns = [
    url(r'^solo/$', views.solo, name='solo'),
    url(r'multi/$', views.multi, name='multi'),
]