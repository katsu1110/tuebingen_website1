from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import whatsnew

# Create your views here.
def index(request):
    return render(request, 'top_page/index.html')

def whatsnew(request):
    whatsnew_list = whatsnew.objects.order_by('-pub_date')[:3]
    context = {'text_title': "What's new?", 'whatsnew_list': whatsnew_list}
    return(request,'top_view/whatsnew.html', context)
