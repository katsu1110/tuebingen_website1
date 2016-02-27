from django.db import models
from django.utils import timezone

# Create your models here.
class Whatsnew(models.Model):
    news_text = models.CharField(max_length=100)
    link_text = models.CharField(max_length=100, default='top_page')
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.news_text
