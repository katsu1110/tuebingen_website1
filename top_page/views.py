from django.shortcuts import render
from django.utils import timezone
from top_page.models import Whatsnew, Upcoming

# Create your views here.
def index(request):
    whatsnews = Whatsnew.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:4]
    upcomings = Upcoming.objects.filter(event_date__gt=timezone.now()).order_by('event_date')[:4]
    context = {'upcomings':upcomings,'whatsnews': whatsnews}
    return render(request, 'top_page/index.html', context)

def positive(request):
    return render(request, 'top_page/positive.html')
