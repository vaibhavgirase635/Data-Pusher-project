from django.contrib import admin
from .models import Myaccount
# Register your models here.
@admin.register(Myaccount)
class MyaccountAdmin(admin.ModelAdmin):
    list_display=['email','account_id','name']
