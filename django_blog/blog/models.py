from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser, BaseUserManager
from taggit.managers import TaggableManager
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profilre')
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)
    
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
