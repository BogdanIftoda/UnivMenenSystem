# Generated by Django 3.1.7 on 2021-05-26 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20210525_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='subjectName',
        ),
    ]
