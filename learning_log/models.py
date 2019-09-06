from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    """Topic, which user meeting"""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Information about step in learning"""
    topic= models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text)>=50:
            self.text=self.text[:50] + "..."
        else:
            self.text
        return self.text


