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


class UserTypeList(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.user_type.name + "_" + self.user.username

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_type', 'user'], name='userTypeList_unique_entry')
        ]
