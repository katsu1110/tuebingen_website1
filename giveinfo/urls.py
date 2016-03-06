from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'giveinfo'
urlpatterns = [
    # /giveinfo/
    url(r'^$', views.middle, name='middle'),
    # /giveinfo/summary/'number'/
    url(r'^summary/$',views.summary,name='summary'),
    # /giveinfo/experience
    url(r'^experience/$',views.experience,name='experience'),
    # /giveinfo/article_top
    url(r'^article_top/$',views.article_top,name='article_top'),
    # /giveinfo/article/'number'/
    url(r'^article/(?P<pk>[0-9]+)/$',views.article,name='article'),
    # /giveinfo/link
    url(r'^link/$',views.link,name='link'),
    # /giveinfo/contact/
    url(r'^contact/$',views.contact,name='contact'),
    # /giveinfo/about/
    url(r'^about/$',views.about,name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
