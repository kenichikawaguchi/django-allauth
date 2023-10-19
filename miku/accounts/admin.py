from django.contrib import admin

from .models import CustomUser, UserType, UserTypeList


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'user_type')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserTypeList)
