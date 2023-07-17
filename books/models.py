from django.db import models


class Library(models.Model):
    sno=models.IntegerField(null=True)
    name=models.CharField(max_length=100) 
    author=models.CharField(max_length=150)
    title=models.CharField(max_length=200)
    number=models.IntegerField(null=True)
    created_time = models.DateTimeField(auto_now_add=True , null = True)
    updated_time = models.DateTimeField(auto_now=True , null = True)
