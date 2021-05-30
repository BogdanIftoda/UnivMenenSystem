# Generated by Django 3.1.7 on 2021-05-26 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20210526_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
            preserve_default=False,
        ),
    ]