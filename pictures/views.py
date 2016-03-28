from django.shortcuts import get_object_or_404, render
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'pictures/index.html')
