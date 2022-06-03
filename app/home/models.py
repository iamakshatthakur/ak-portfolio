# # from contextlib import nullcontext
# # from pyexpat import model
# # from random import choices
# from ctypes import addressof
from django.db import models

# Create your models here.
mainuser=[("user","mainuser")]
skillset=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6")]
class main_user(models.Model):
    user=models.CharField(choices=mainuser,null=False,blank=False,max_length=50,unique=True)
    name=models.CharField(null=False,blank=False,max_length=50)
    address=models.CharField(null=False,blank=False,max_length=200)
    role=models.CharField(null=False,blank=False,max_length=50)
    phone=models.CharField(max_length=13)
    background_img=models.FileField(upload_to='documents/')
    emailid=models.CharField(null=False,blank=False,max_length=50)
    github=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)

class about(models.Model):
    user_img=models.FileField(upload_to='documents/')
    user=models.CharField(choices=mainuser,null=False,blank=False,max_length=50)
    about_heading=models.CharField(max_length=100)
    about=models.CharField(max_length=1000)
    resume=models.FileField(upload_to='documents/')

class Projects(models.Model):
    frontend360pimg=models.FileField(upload_to='documents/' , blank=False)
    frontend720pimg=models.FileField(upload_to='documents/' , blank=False)
    frontend1080pimg=models.FileField(upload_to='documents/' , blank=False)
    adminloginimg=models.FileField(upload_to='documents/' , blank=False)
    adminpanelimg=models.FileField(upload_to='documents/' , blank=False)
    aboutproject1=models.CharField(max_length=500)
    aboutproject2=models.CharField(max_length=500)
    aboutproject3=models.CharField(max_length=500)
    aboutproject4=models.CharField(max_length=500)
    
class Skill(models.Model):
    skillid=models.CharField(choices=skillset,max_length=50,unique=True)
    logo=models.CharField(max_length=50)
    skill=models.CharField(max_length=50)
    skill_description=models.CharField(max_length=50)
    
class contactmessage(models.Model):
    sender_name=models.CharField(max_length=50)
    sender_email=models.CharField(max_length=50)
    sender_subject=models.CharField(max_length=100)
    sender_message=models.CharField(max_length=500)
    def sentmessage(self):
        self.save()