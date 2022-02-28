from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.hello,name="index"),
]


