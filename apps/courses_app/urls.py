from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.add),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^remove/(?P<id>\d+)$', views.delete)
]
