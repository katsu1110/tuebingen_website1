from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from top_page.models import Whatsnew, Upcoming

# Create your views here.
def index(request):
    whatsnews = Whatsnew.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:4]
    upcomings = Upcoming.objects.all()[:4]
    context = {'upcomings':upcomings,'whatsnews': whatsnews}
    return render(request, 'top_page/index.html', context)

def positive(request):
    return render(request, 'top_page/positive.html')
