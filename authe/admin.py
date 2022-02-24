from django.contrib import admin
from .models import ConfirmationCode,User


# Register your models here.
class ConfirmationCodeAdmin(admin.ModelAdmin):
   list_display = ['code' , 'id']
admin.site.register(ConfirmationCode,ConfirmationCodeAdmin)
# @admin.register(ConfirmationCode)
# class ConfirmationCodeAdmin(admin.ModelAdmin):
#    list_display = ['code' , 'id']

admin.site.register(User)
