from django.contrib import admin
from .models import Summary, Experience, Experiencetext, Article, Articletext, Link
#from django_summernote.admin import SummernoteModelAdmin

#class SummaryAdmin(admin.ModelAdmin):
#    change_form_template = 'giveinfo/admin/change_form.html'

#class ExperienceAdmin(admin.ModelAdmin):
#    change_form_template = 'giveinfo/admin/change_form.html'

#class ArticleAdmin(admin.ModelAdmin):
#    change_form_template = 'giveinfo/admin/change_form.html'

#admin.site.register(Summary,SummaryAdmin)
#admin.site.register(Experience,ExperienceAdmin)
#admin.site.register(Article,ArticleAdmin)
admin.site.register(Summary)
admin.site.register(Experience)
admin.site.register(Experiencetext)
admin.site.register(Article)
admin.site.register(Articletext)
admin.site.register(Link)

#admin.site.register(Experiencetext,ExperiencetextAdmin)
#admin.site.register(Articletext,ArticletextAdmin)
