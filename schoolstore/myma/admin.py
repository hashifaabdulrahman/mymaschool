from django.contrib import admin
from .models import Student,Department,Courses,Enquiry

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Enquiry)