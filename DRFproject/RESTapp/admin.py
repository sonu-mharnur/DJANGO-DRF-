from django.contrib import admin
from .models import Student
from.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Categoty)
admin.site.register(Book)



# @admin.register(Student)
# class Student(admin.ModelAdmin):
#     list_display = ('Name', 'Age','Father' )
    
