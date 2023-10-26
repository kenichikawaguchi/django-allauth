from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('user/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
]
