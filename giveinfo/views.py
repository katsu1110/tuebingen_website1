from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse
#from django.template import loader
from django.utils import timezone
from .models import Summary, Experience, Article, Link, Experiencetext, Articletext
# ExperienceText, ArticleText
# Create your views here.

def middle(request):
    experiences = Experience.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    articles = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    links = Link.objects.all()
    context = {'experiences':experiences,'articles':articles,'links':links}
    return render(request, 'giveinfo/middle.html',context)

def summary(request):
    return render(request, 'giveinfo/summary.html')

def experience_top(request):
    posts = Experience.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    context = {'posts': posts}
    return render(request, 'giveinfo/experience_top.html', context)

def experience(request,experience_id):
    posts = get_object_or_404(Experience,pk=experience_id)
    context = {'posts': posts}
    return render(request, 'giveinfo/experience.html', context)

def article_top(request):
    posts = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    context = {'posts': posts}
    return render(request, 'giveinfo/article_top.html', context)

def article(request,article_id):
    posts = get_object_or_404(Article,pk=article_id)
    context = {'posts': posts}
    return render(request, 'giveinfo/article.html', context)

def link(request):
    posts = Link.objects.all()
    context = {'posts': posts}
    return render(request, 'giveinfo/link.html', context)

def contact(request):
    context = {'text_title': 'コンタクト'}
    return render(request,'giveinfo/contact.html', context)

def about(request):
    context = {'text_title': 'このホームページについて'}
    return render(request,'giveinfo/about.html', context)

#def whatsnew(request,whatsnew_id):
#    post = get_object_or_404(Article,article_id=article_id)
#    text_title = "What's new?"
#    context = {'text_title': text_title, 'posts': posts}
#    return render(request, 'giveinfo/whatsnew.html', context)
