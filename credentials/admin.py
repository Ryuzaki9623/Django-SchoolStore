from django.contrib import admin

# Register your models here.
from .models import Department, Course, Purpose

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['depname']
admin.site.register(Department, DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['crsname', 'depid']
admin.site.register(Course, CourseAdmin)

class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Purpose, PurposeAdmin)