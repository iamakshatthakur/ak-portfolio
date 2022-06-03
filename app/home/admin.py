from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(main_user)
class main_userAdmin(admin.ModelAdmin):
    list_display=['user','name','address','emailid','phone','role','github','instagram','linkedin']
@admin.register(about)
class aboutAdmin(admin.ModelAdmin):
    list_display=['user','about_heading','about','resume']
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display=['frontend360pimg','frontend720pimg','frontend1080pimg','adminloginimg','adminpanelimg','aboutproject1','aboutproject2','aboutproject3','aboutproject4']
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['skillid','logo','skill','skill_description']
@admin.register(contactmessage)
class contactmessageAdmin(admin.ModelAdmin):
    list_display=['sender_name','sender_email','sender_subject','sender_message']
