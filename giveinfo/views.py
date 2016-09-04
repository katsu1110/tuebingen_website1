from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Summary, Experience, Article, Link, Experiencetext, Articletext, ImageUpload
from .forms import SubmitForm
from django.core.mail import send_mail
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
    form = SubmitForm()
    message = ''
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            like = form.cleaned_data['like']
            dislike = form.cleaned_data['dislike']
            others = form.cleaned_data['others']
            agree = form.cleaned_data['agree']
            image = form.cleaned_data['image']

            texts = dislike + ' / ' + like + ' / ' + others
            recipients = ['code1110g-show@hotmail.co.jp']

            if cc_myself:
                recipients.append(email)

            send_mail(your_name, texts, email, recipients, fail_silently=False)
            message = 'ありがとうございます。内容は送信されました！'

        else:
            message = 'どこかにエラーがあります。送信されませんでした。'
            form = SubmitForm()

    context = {'text_title': 'コンタクト', 'form': form, 'message': message}
    return render(request,'giveinfo/contact.html', context)

def about(request):
    context = {'text_title': 'このホームページについて'}
    return render(request,'giveinfo/about.html', context)

#def whatsnew(request,whatsnew_id):
#    post = get_object_or_404(Article,article_id=article_id)
#    text_title = "What's new?"
#    context = {'text_title': text_title, 'posts': posts}
#    return render(request, 'giveinfo/whatsnew.html', context)
