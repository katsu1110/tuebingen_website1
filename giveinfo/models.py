from django.db import models

# Create your models here.

class Summary(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10)
    main_text = models.CharField(max_length=500)

    def __str__(self):
        return self.main_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Experience(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10)
    main_text = models.CharField(max_length=500)

    def __str__(self):
        return self.main_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Article(models.Model):
    text_title = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10)
    main_text = models.CharField(max_length=500)

    def __str__(self):
        return self.main_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
