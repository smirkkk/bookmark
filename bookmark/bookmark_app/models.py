from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(default=None, null=True, blank=True, max_length=100)
    url = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title