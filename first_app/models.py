from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=15)
  email = models.CharField(max_length=20)
  password = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Card(models.Model):
  title = models.CharField(max_length=15)
  author = models.ForeignKey(User, related_name="cards", on_delete = models.CASCADE)
  content = models.TextField()
  image = models.TextField()
  link = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)