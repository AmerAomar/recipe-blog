from django.db import models
from accounts.models import CustomUser
# Create your models here.
class recipe(models.Model):
    name=models.CharField(max_length=100)
    cheff=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    ingredients=models.TextField()
    steps=models.TextField()