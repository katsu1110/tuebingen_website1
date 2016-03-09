from django.db import models
from django.utils import timezone
#from tinymce.models import HTMLField

# Create your models here.
class Summary(models.Model):
    head = models.CharField(max_length=100, default='')
    sub_head = models.CharField(max_length=100, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    main_text = models.TextField()
    img = models.ImageField(upload_to='images',
    default='')

    def __str__(self):
        return self.main_text

class Experience(models.Model):
    text_title = models.CharField(max_length=100, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=50, default='管理人')

    def __str__(self):
        return self.text_title

class ExperienceText(models.Model):
    experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    main_text = models.TextField()


class Article(models.Model):
    text_title = models.CharField(max_length=100, default='')
    pub_date = models.DateTimeField(blank=True, null=True)
    writer = models.CharField(max_length=50, default='管理人')
    #img = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.text_title

class ArticleText(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    main_text = models.TextField()

class Link(models.Model):
    link_title = models.CharField(max_length=100)
    link_text = models.CharField(max_length=200)
    urllink = models.URLField(max_length=200)

    def __str__(self):
            return self.link_title
