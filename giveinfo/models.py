from django.db import models
from django.utils import timezone

# Create your models here.
class Summary(models.Model):
    head = models.CharField(max_length=20, default='')
    sub_head = models.CharField(max_length=50, default='')
    main_text = models.TextField()
    correspond_img = models.ImageField(upload_to='uploads/',
    height_field=100,width_field=162,max_length=30,default='')

    def __str__(self):
        return self.main_text

class Experience(models.Model):
    text_title = models.CharField(max_length=40, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10, default='管理人')
    main_text = models.TextField()

    def __str__(self):
        return self.text_title

class Article(models.Model):
    text_title = models.CharField(max_length=40, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=10, default='管理人')
    main_text = models.TextField()
    correspond_img = models.ImageField(upload_to='uploads/',
    height_field=200,width_field=324,max_length=30,default='')

    def __str__(self):
        return self.text_title

class Link(models.Model):
    link_title = models.CharField(max_length=30)
    link_text = models.CharField(max_length=100)
    urllink = models.URLField(max_length=100)

    def __str__(self):
            return self.text_title
