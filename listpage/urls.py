
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.get_joblist, name='url'),
    url('list', views.get_joblist, name='list'),
]
