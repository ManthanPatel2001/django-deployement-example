from operator import truediv
from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.EmailField(max_length=260,unique=True)

