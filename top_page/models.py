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

class Upcoming(models.Model):
    event_date = models.DateTimeField(blank=True, null=True)
    event_venue = models.CharField(max_length=100)
    venue_link = models.URLField(max_length=200)
    event_text = models.CharField(max_length=100)

    def publish(self):
        self.event_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_text
