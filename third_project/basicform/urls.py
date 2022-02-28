from django.urls import path
from basicform import views

urlpatterns = [
    path('index/',views.basic,name='basic'),
]