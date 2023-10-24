from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    short_intro = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField( null=True, blank=True, max_length=22)
    description = models.TextField(max_length=400, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_twitter = models.CharField(max_length=400, null=True, blank=True)
    social_github = models.CharField(max_length=400, null=True, blank=True)
    social_linkedin = models.CharField(max_length=400, null=True, blank=True)
    social_website = models.CharField(max_length=400, null=True, blank=True)
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique= True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)

class Skill (models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, unique= True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)







