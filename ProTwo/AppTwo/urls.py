from unicodedata import name
from django.urls import path
from AppTwo import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('help/',views.help,name="help"),
    path('users/',views.users,name="users"),
    path('signup/',views.signup,name="signup"),
]


