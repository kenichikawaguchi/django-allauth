from django.contrib import admin

from .models import CustomUser, UserType


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType)
