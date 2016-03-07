from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Summary(models.Model):
    head = models.CharField(max_length=20, default='')
    sub_head = models.CharField(max_length=50, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    main_text = HTMLField()
    img = models.ImageField(upload_to='images',
    default='')

    def __str__(self):
        return self.main_text

class Experience(models.Model):
    text_title = models.CharField(max_length=40, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10, default='管理人')
    main_text = HTMLField()

    def __str__(self):
        return self.text_title

class Article(models.Model):
    text_title = models.CharField(max_length=40, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10, default='管理人')
    main_text = HTMLField()
    img = models.ImageField(upload_to='images',
    default='')

    def __str__(self):
        return self.text_title

class Link(models.Model):
    link_title = models.CharField(max_length=30)
    link_text = models.CharField(max_length=100)
    urllink = models.URLField(max_length=100)

    def __str__(self):
            return self.link_title
