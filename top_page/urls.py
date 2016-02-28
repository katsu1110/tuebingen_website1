from django.conf.urls import url
from . import views

app_name = 'top_page'
urlpatterns = [
    # /top_page/
    url(r'^$',views.index,name='index'),
    # /top_page/positive/
    url(r'^positive/$',views.positive,name='positive'),
]
