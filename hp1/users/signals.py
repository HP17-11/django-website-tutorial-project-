from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 

from django.db import models
from django.contrib.auth.models import User
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    print("ttttttttttttttttt")
    if created:
        user = instance
        profile = Profile.objects.create ( 
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            )

def updateuser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteuser(sender, instance, **kwargs):
    user = instance.user 
    #print(user)
    user.delete()
       
post_save.connect(createProfile, sender = User)
post_save.connect(updateuser, sender = Profile)
post_delete.connect(deleteuser, sender = Profile)