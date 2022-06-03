from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.
 
def index(request):
    adminuser=main_user.objects.all()
    aboutuser=about.objects.all()
    projects=Projects.objects.all()
    userskills=Skill.objects.all()
    if (len(main_user.objects.all())>0):
        adminuser=main_user.objects.all()[0]
    if (len(about.objects.all())>0):
        aboutuser=about.objects.all()[0]
    if request.method=="POST":
        sendername=request.POST["sendername"]
        senderemail=request.POST["senderemail"]
        messagesubject=request.POST["messagesubject"]
        message=request.POST["message"]
        send_mail(
                    messagesubject,
                    message + " from "+sendername + " the mail id of user is " + senderemail,
                    'sample.mail.ak@gmail.com',
                    ['akthakur7865@gmail.com'],
                    fail_silently=False,
                    )
        clientmessage=contactmessage( sender_name=sendername,sender_email=senderemail,sender_subject=messagesubject,sender_message=message)
        clientmessage.sentmessage()
    return render(request,'index.html',{'user':adminuser ,'about':aboutuser,'skills':userskills,'projects':projects})