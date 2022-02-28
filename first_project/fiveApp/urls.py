from django.conf.urls import url
from fiveApp import views
app_name = 'fiveApp'
urlpatterns = [
    url('index/',views.index,name='index'),
    url('reg/',views.register,name='register'),
    url('login/',views.user_login,name='user_login'),
    url('logout/',views.user_logout,name='user_logout'),
    url('special/',views.special,name='special'),
    
]