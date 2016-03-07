from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse
#from django.template import loader
from django.utils import timezone
from .models import Summary, Experience, Article, Link
# Create your views here.

def middle(request):
    experiences = Experience.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    articles = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    links = Link.objects.all()
    context = {'experiences':experiences,'articles':articles,'links':links}
    return render(request, 'giveinfo/middle.html',context)

def summary(request):
    posts = Summary.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'giveinfo/summary.html', context)

def experience(request):
    posts = Experience.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    theme_category = '生活お役立ち情報'
    smalltext_title = '留学・滞在体験記'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'posts': posts}
    return render(request, 'giveinfo/experience.html', context)

def article_top(request):
    posts = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    theme_category = '生活お役立ち情報'
    smalltext_title = '役に立つコラム'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'posts': posts}
    return render(request, 'giveinfo/article_top.html', context)

def article(request):
    posts = get_object_or_404(Article,pk=Article.id)
    theme_category = '生活お役立ち情報'
    smalltext_title = '役に立つコラム'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'posts': posts}
    return render(request, 'giveinfo/article.html', context)

def link(request):
    posts = Link.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    theme_category = '生活お役立ち情報'
    smalltext_title = '役に立つリンク集'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'posts': posts}
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
