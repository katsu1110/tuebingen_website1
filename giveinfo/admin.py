from django.contrib import admin

from .models import Summary, Experience, Article, Link

admin.site.register(Summary)
admin.site.register(Experience)
admin.site.register(Article)
admin.site.register(Link)
