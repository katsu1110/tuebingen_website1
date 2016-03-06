from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'pictures'
urlpatterns = [
    # /pictures/
    url(r'^$', views.index, name='index'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
