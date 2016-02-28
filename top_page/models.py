from django.db import models
from django.utils import timezone

# Create your models here.
class Whatsnew(models.Model):
    news_text = models.CharField(max_length=100)
    link_text = models.CharField(max_length=100, default='top_page')
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.news_text

class Positive(models.Model):
    jp = models.CharField(max_length=100, default='きっといいことあるよ！')
    de = models.CharField(max_length=100, default='Viel glückwünsche bei dir!')
    en = models.CharField(max_length=100, default='May you have something wonderful!')
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.jp
