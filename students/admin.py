from django.contrib import admin

from .models import Student, Subject, Specialty
# Register your models here.

admin.site.register(Specialty)
admin.site.register(Student)
admin.site.register(Subject)
