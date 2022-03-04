from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Question(models.Model):
    """Highway signs template [qs -> question]"""
    QS_TYPE_CHOICES = (('General', 'General'),
                        ('Definition', 'Definition'),
                        ('Signs', 'Signs'),
                        ('Mtb', 'Mtb'))
    qs_title = models.CharField(max_length=1000, unique=True)
    qs_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    qs_type = models.CharField(max_length=1000, choices=QS_TYPE_CHOICES)
    qs_answer = models.TextField()
    qs_date_added = models.DateTimeField(default=datetime.now, blank=True)
    qs_likes = models.ManyToManyField(User, related_name='questions_like')
    qs_dislikes = models.IntegerField(default=0)


    def total_likes(self):
        """count no. of likes"""
        return self.qs_likes.count()

    def __str__(self):
        """Return a string rep of the sign"""
        return f'{self.id}. {self.qs_title}'
