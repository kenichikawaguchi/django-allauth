# Generated by Django 4.2.5 on 2023-10-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_lesson_student_alter_lesson_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name=''),
        ),
    ]