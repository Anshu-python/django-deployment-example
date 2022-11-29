from django.shortcuts import render,HttpResponse
from datetime import datetime
from members.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {'variable1':'Bej','variable2':'This is sent via context variable from views-->template'}
    return render(request,"index.html",context)
    #return HttpResponse("This is Family Members HOME page!!")

def about(request):
    return render(request,"about.html")
    #return HttpResponse("This is Family Members ABOUT page!!")

def business(request):
    return render(request,"business.html")
    #return HttpResponse("This is Family Members BUSINESS page!!")

def contact(request):
    print("The request method is :",request.method)
    if request.method == 'POST':
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        desc = request.POST.get("Desc")
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your details has been sent!!')

    return render(request,"contact.html")
    #return HttpResponse("This is Family Members CONTACT page!!")
