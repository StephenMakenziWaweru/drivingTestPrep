from audioop import maxpp
from tkinter.messagebox import IGNORE
from tokenize import Ignore
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
# Create your models here.
class Sign(models.Model):
    """Highway signs template [hs -> Highway Sign]"""
    HS_TYPE_CHOICES = (('Class A', 'Class A'),
                        ('Class B', 'Class B'),
                        ('Class C', 'Class C'))
    hs_id = models.TextField(default=uuid4, blank=True, primary_key=True)
    hs_title = models.TextField(max_length=100, unique=True)
    hs_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hs_type = models.TextField(max_length=100, choices=HS_TYPE_CHOICES)
    hs_image = models.ImageField(upload_to='highway_signs')
    hs_date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """Return a string rep of the sign"""
        return self.hs_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.hs_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
