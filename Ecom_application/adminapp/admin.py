from django.contrib import admin
from adminapp.models import *

# Register your models here.

@admin.register((Adminuser))
class AdminuserModelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','password','is_active','adress','image']                 

