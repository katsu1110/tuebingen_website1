from django.db import models

# Create your models here.
class whatsnew(models.Model):
    news_text = models.CharField(max_length=100)
    new_date = models.DateTimeField('date published')
