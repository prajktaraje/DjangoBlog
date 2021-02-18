from django.db.models.fields import DateTimeCheckMixin
from django.shortcuts import render
from .models import Blogpost, Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/home.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})

def contact(request):
    # return HttpResponse("This is contact page")  
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        

        if len(email)<4 or len(name)<3 or len(desc)<5:
            messages.error(request,"Please fill the form currectly..!")
        else:
            contact=Contact(email=email,name=name,desc=desc,date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been successfully sent")    
       
       
    return render(request,'blog/contact.html')