from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname","joining_date", "phone" )

admin.site.register(Student, StudentAdmin)
