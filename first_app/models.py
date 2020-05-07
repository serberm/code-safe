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

class Idea_Bug(models.Model):
  author = models.ForeignKey(User, related_name="ideas_bugs", on_delete = models.CASCADE)
  content = models.TextField()
  idea = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  author = models.ForeignKey(User, related_name="comments_author", on_delete = models.CASCADE)
  post = models.ForeignKey(Idea_Bug, related_name="comments_post", on_delete = models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)