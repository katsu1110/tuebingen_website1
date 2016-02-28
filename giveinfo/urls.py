from django.conf.urls import url
from . import views


app_name = 'giveinfo'
urlpatterns = [
    # /giveinfo/
    url(r'^$', views.middle, name='middle'),
    # /giveinfo/summary/'number'/
    url(r'^summary/$',views.summary,name='summary'),
    # /giveinfo/experience/'number'/
    url(r'^experience/(?P<experience_id>[0-9]+)/$',views.experience,name='experience'),
    # /giveinfo/article/'number'/
    url(r'^article/(?P<article_id>[0-9]+)/$',views.article,name='article'),
    # /giveinfo/link
    url(r'^link/$',views.link,name='link'),
    # /giveinfo/contact/
    url(r'^contact/$',views.contact,name='contact'),
    # /giveinfo/about/
    url(r'^about/$',views.about,name='about'),
]
