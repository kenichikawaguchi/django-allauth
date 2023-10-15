from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('custom_date_display', 'teacher', 'student', 'booking')

    def custom_date_display(self, obj):
        return obj.time.strftime("%Y-%m-%d %H:%M:%S")


admin.site.register(Lesson, LessonAdmin)

