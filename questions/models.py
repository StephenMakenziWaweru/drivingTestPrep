from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    """Highway signs template [qs -> question]"""
    QS_TYPE_CHOICES = (('General', 'General'),
                        ('Definition', 'Definition'),
                        ('Signs', 'Signs'),
                        ('Mtb', 'Mtb'))
    qs_title = models.CharField(max_length=1000, unique=True, verbose_name=u"Question")
    qs_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    qs_type = models.CharField(max_length=1000, choices=QS_TYPE_CHOICES, verbose_name=u"Type")
    qs_answer = models.TextField(verbose_name=u"Answer")
    qs_date_added = models.DateTimeField(default=datetime.now, blank=True)
    qs_likes = models.ManyToManyField(User, related_name='questions_like', blank=True)
    qs_dislikes = models.ManyToManyField(User, related_name='questions_dislike', blank=True)

    class Meta:
        ordering = ["-id"]

    def total_likes(self):
        """count no. of likes"""
        return self.qs_likes.count()

    def total_dislikes(self):
        """count no. of dislikes"""
        return self.qs_dislikes.count()

    def __str__(self):
        """Return a string rep of the sign"""
        return f'{self.id}. {self.qs_title}'

    def get_absolute_url(self):
        """returns the url of a Question detail view"""
        return reverse('question-detail', kwargs={'pk': self.pk})
