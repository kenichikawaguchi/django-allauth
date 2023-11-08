from django.contrib import admin

from .models import CustomUser, UserType, UserTypeList
from allauth.account.models import EmailAddress


class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 1


class UserTypeListInline(admin.TabularInline):
    model = UserTypeList
    extra = 1


class UserTypeListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type', 'user')


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', )
    readonly_fields = ('date_joined', )
    inlines = [UserTypeListInline, EmailAddressInline]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserTypeList, UserTypeListAdmin)
