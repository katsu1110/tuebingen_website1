from django.conf.urls import url

from top_page import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^whatsnew/$',views.whatsnew,name='whatsnew'),
]
