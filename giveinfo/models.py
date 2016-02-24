from django.db import models
from django.utils import timezone

# Create your models here.
class Summary(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10)
    main_text = models.TextField()

    def __str__(self):
        return self.text_title

class Experience(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10)
    main_text = models.TextField()

    def __str__(self):
        return self.text_title

class Article(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10)
    main_text = models.TextField()

    def __str__(self):
        return self.text_title
