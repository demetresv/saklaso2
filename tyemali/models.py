from django.db import models
import datetime



class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date= models.DateField()
    edited = models.BooleanField()
    write_date = models.DateTimeField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

class Category(models.Model):
    name=models.CharField(max_length=100)