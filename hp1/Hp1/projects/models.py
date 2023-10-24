from uuid import uuid4
from django.db import models
from users.models import Profile


# Create your models here.

class Project (models.Model):
    
    title = models.CharField(max_length = 200)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    featured_image = models.ImageField( null=True, blank=True, default='default.jpg')
    demolink = models.CharField(max_length=200, null=True, blank=True)
    sourcecode = models.CharField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    votes_total = models.IntegerField(default=0, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return self.title

class Review (models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    VOTE_TYPE =(('up','up vote'),('down','down vote'))
    body = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length = 200, choices=VOTE_TYPE)
 

    def __str__(self):
        return self.value

class Tag(models.Model):

    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


