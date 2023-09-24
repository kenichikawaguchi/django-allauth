from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', 'teacher', 'student', 'booking')


admin.site.register(Lesson, LessonAdmin)

