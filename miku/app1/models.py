from django.db import models
from accounts.models import CustomUser


class Lesson(models.Model):
    name = models.CharField(
        verbose_name='',
        blank=True,
        null=True,
        max_length=50,
        default='')
    time = models.DateTimeField()
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True, related_name="teacher")
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True, related_name="student")
    booking = models.BooleanField(default=False)


    def __str__(self):
        lesson_str = str(self.id) + "_" + self.teacher.username 
        return lesson_str
