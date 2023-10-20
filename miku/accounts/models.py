from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT, null=True)
    email = models.EmailField(unique=True)
    class Meta:
        verbose_name_plural = 'CustomUser'


