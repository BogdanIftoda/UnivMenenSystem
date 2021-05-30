# Generated by Django 3.1.7 on 2021-05-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_student_averagemark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='averageMark',
        ),
        migrations.AddField(
            model_name='subject',
            name='averageMark',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
