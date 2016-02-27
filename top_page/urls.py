from django.conf.urls import url
from . import views

app_name = 'top_page'
urlpatterns = [
    url(r'^$',views.index,name='index'),
]
