from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    context = {'text_title': '写真館'}
    return render(request, 'pictures/index.html',context)
