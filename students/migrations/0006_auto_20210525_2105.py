# Generated by Django 3.1.7 on 2021-05-25 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_specialty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='midleName',
            new_name='middleName',
        ),
    ]
