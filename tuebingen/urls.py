"""tuebingen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^top_page/',include('top_page.urls',namespace='top_page')),
    url(r'^giveinfo/',include('giveinfo.urls',namespace='giveinfo')),
    url(r'^pictures/',include('pictures.urls',namespace='pictures')),
    url(r'^stress/',include('stress.urls',namespace='stress')),
    #url(r'^summernote/', include('django_summernote.urls')),
    #url(r'^tinymce/',include('tinymce.urls')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)
