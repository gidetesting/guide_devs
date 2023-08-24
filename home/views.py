from django.shortcuts import render
from home.models import info,basic,intermediate,premium
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Infe = info(name=name,email=email,subject=subject)
        Infe.save()
        messages.success(request,'Message has been sent')
    return render(request,'index.html')

def basi(request):
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            bas = basic(name=name,email=email,subject=subject,phone=phone)
            bas.save()
            messages.success(request,"basic plan has been applied")
    return render(request,'basic.html')

def inter(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            itr = intermediate(name=name,email=email,subject=subject,phone=phone)
            itr.save()
        return render(request,'inter.html')

def premiu(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        pre = premium(name=name,email=email,subject=subject,phone=phone)
        pre.save()
    return render(request,'premium.html')

def pofo(request):
    return render(request,'portfolio.html')
