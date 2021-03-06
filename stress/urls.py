from django.conf.urls import url
from django.conf import settings
from . import views


app_name = 'stress'
urlpatterns = [
    # /stress/
    url(r'^$', views.index, name='index'),
    # /stress/check1/
    url(r'^check1/$',views.check1,name='check1'),
    # /stress/check1/
    url(r'^check2/$',views.check2,name='check2'),
    # /stress/check1/
    url(r'^check3/$',views.check3,name='check3'),
    # /stress/check1/
    url(r'^check4/$',views.check4,name='check4'),
    # /stress/check1/
    url(r'^check5/$',views.check5,name='check5'),
    # /stress/check1/
    url(r'^check6/$',views.check6,name='check6'),
    # /stress/check1/
    url(r'^check7/$',views.check7,name='check7'),
    # /stress/johari/
    url(r'^johari/$',views.johari,name='johari'),
    # /stress/johari/
    url(r'^middle/$',views.middle,name='middle'),
    # /stress/johari/
    url(r'^watari/$',views.watari,name='watari'),
    # /stress/cognitive/
    url(r'^cognitive/$',views.cognitive,name='cognitive'),

    ]

    #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
