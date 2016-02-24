from django.shortcuts import get_object_or_404, render

from giveinfo.models import Summary, Experience, Article
# Create your views here.

def middle(request):
    context = {'text_title': 'お役立ち情報'}
    return render(request, 'giveinfo/middle.html',context)

def summary(request,summary_id):
    post = get_object_or_404(Summary,summary_id=summary_id)
    theme_category = 'チュービンゲンについてのまとめ'
    smalltext_title = ''
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title, 'post': post}
    return render(request, 'giveinfo/simple_text.html', context)

def experience(request,experience_id):
    post = get_object_or_404(Experience,experince_id=experince_id)
    theme_category = '生活お役立ち情報'
    smalltext_title = '留学・滞在体験記'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'post': post}
    return render(request, 'giveinfo/simple_text.html', context)

def article(request,article_id):
    post = get_object_or_404(Article,article_id=article_id)
    theme_category = '生活お役立ち情報'
    smalltext_title = '生活コラム'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'post': post}
    return render(request, 'giveinfo/simple_text.html', context)

def contact(request):
    context = {'text_title': 'コンタクト'}
    return(request,'giveinfo/contact.html', context)

def about(request):
    context = {'text_title': 'このホームページについて'}
    return(request,'giveinfo/contact.html', context)

def whatsnew(request,whatsnew_id):
    post = get_object_or_404(Article,article_id=article_id)
    text_title = "What's new?"
    context = {'text_title': text_title, 'post': post}
    return render(request, 'giveinfo/whatsnew.html', context)
