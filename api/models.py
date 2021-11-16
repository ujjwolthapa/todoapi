from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    
    class Meta:
        ordering = ['-updated']