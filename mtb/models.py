from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Notes(models.Model):
    """Defines attributes of an mtb notes addition"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    owner = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        """Returns a string rep of the model"""
        return f'{self.title} notes'


class Video(models.Model):
    """Defines a video attributes"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        """Returns a string rep of the model"""
        return f'{self.title} video'
