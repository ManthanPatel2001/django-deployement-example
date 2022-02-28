from django.conf.urls import url
from fourApp import views

app_name = 'fourApp'

urlpatterns = [
    url("index/",views.index,name='index'),
    url("other/",views.other,name='other'),
]
