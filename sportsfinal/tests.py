
from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
# Create your views here.
def indexPage(request):
    return render(request,"app/index.html")


def regUser(request):
    fnm=request.POST['fname']
    lnm=request.POST['lname']
    em=request.POST['email']
    psw=request.POST['password']
    profilepic=request.FILES['image']

    newUser=Users.objects.create(firstname=fnm, lastname=lnm,email=em,password=psw,profile_pic=profilepic)
    return HttpResponseRedirect(reverse('showdetails'))


def show_details(request):
    all_users = Users.objects.all()
    return render(request,"app/success.html",{'key1':all_users})