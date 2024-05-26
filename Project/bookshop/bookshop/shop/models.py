from django.db import models


class User(models.Model):
  username = models.CharField(max_length=255)
  userid = models.AutoField(primary_key=True)
  password_hash = models.CharField(max_length=255)
  phone = models.CharField(max_length=11, default="")

  
class Book(models.Model):
    name = models.CharField(max_length=255)
    bookid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, default="other")
    description = models.CharField(max_length=1000, default="")
    price = models.IntegerField(default=80000)


