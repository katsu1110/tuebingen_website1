from django.shortcuts import render
from django.template import loader
from .models import Whatsnew

# Create your views here.
def index(request):
    whatsnew = Whatsnew.objects.order_by('-pub_date')
    context = {'whatsnew': whatsnew}
    return render(request, 'top_page/index.html', context)
