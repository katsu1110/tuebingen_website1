from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'top_page'
urlpatterns = [
    # /top_page/
    url(r'^$',views.index,name='index'),
    # /top_page/positive/
    url(r'^positive/$',views.positive,name='positive'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
