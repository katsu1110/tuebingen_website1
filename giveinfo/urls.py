from django.conf.urls import url
#from django.conf import settings
#from django.conf.urls.static import static
from . import views


app_name = 'giveinfo'
urlpatterns = [
    # /giveinfo/
    url(r'^$', views.middle, name='middle'),
    # /giveinfo/summary/
    url(r'^summary/$',views.summary,name='summary'),
    # /giveinfo/article_top/
    url(r'^experience_top/$',views.experience_top,name='experience_top'),
    # /giveinfo/experience/'id'/
    url(r'^experience/(?P<experience_id>[0-9]+)/$',views.experience,name='experience'),
    # /giveinfo/article_top/
    url(r'^article_top/$',views.article_top,name='article_top'),
    # /giveinfo/article/'id'/
    url(r'^article/(?P<article_id>[0-9]+)/$',views.article,name='article'),
    # /giveinfo/link/
    url(r'^link/$',views.link,name='link'),
    # /giveinfo/contact/
    url(r'^contact/$',views.contact,name='contact'),
    # /giveinfo/about/
    url(r'^about/$',views.about,name='about'),
]

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
