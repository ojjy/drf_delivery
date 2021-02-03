from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=256)
    detailAddress = models.CharField(max_length=256)
    extraAddress = models.CharField(max_length=256)
    postcode = models.CharField(max_length=16)
