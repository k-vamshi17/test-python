from django.contrib import admin
from testapp import models
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['Rollno','Name','Email','PhoneNo']
admin.site.register(models.student,studentadmin)