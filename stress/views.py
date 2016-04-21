from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stress/index.html')

def check1(request):
    return render(request, 'stress/check1.html')

def check2(request):
    return render(request, 'stress/check2.html')

def check3(request):
    return render(request, 'stress/check3.html')

def check4(request):
    return render(request, 'stress/check4.html')

def check5(request):
    return render(request, 'stress/check5.html')

def check6(request):
    return render(request, 'stress/check6.html')

def check7(request):
    return render(request, 'stress/check7.html')

def johari(request):
    return render(request, 'stress/johari.html')
