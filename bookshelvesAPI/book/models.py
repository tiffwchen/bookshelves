from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.CharField(max_length=1000)
    page_count = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title