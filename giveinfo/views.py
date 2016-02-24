from django.shortcuts import get_object_or_404, render

from giveinfo.models import Summary, Experience, Article
# Create your views here.

def middle(request):
    context = {'text_title': 'お役立ち情報'}
    return render(request, 'giveinfo/middle.html',context)

def summary(request,summary_id):
    text_list = Summary.objects[:10]
    theme_category = 'チュービンゲンについてのまとめ'
    smalltext_title = ''
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title, 'text_list': text_list, 'text_title': Summary.text_title,
    'pub_data': Summary.pub_date, 'writer': Summary.writer, 'main_text': Summary.main_text}
    return render(request, 'giveinfo/simple_text.html', context)

def experience(request,experience_id):
    text_list = Experience.objects[:5]
    theme_category = '生活お役立ち情報'
    smalltext_title = '留学・滞在体験記'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'text_list': text_list, 'text_title': Experience.text_title,
    'pub_data': Experience.pub_date, 'writer': Experience.writer, 'main_text': Experience.main_text}
    return render(request, 'giveinfo/simple_text.html', context)

def article(request,article_id):
    text_list = Article.objects[:5]
    theme_category = '生活お役立ち情報'
    smalltext_title = '生活コラム'
    context = {'theme_category': theme_category, 'smalltext_title': smalltext_title,'text_list': text_list, 'text_title': Article.text_title,
    'pub_data': Article.pub_date, 'writer': Article.writer, 'main_text': Article.main_text}
    return render(request, 'giveinfo/simple_text.html', context)

def contact(request):
    context = {'text_title': 'コンタクト'}
    return(request,'giveinfo/contact.html', context)

def about(request):
    context = {'text_title': 'このホームページについて'}
    return(request,'giveinfo/contact.html', context)
