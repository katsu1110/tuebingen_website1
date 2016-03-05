from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Imagepost
# Create your views here.

def index(request):
    posts = Imagepost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'pictures/index.html', context)
