from django.contrib import admin
from .models import Course, Project, SyllabusItem

admin.site.register(Course)
admin.site.register(Project)
admin.site.register(SyllabusItem)