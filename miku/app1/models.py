from django.db import models
from accounts.models import CustomUser


class Lesson(models.Model):
    time = models.DateTimeField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True, related_name="teacher")
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True, related_name="student")
    booking = models.BooleanField(default=False)
