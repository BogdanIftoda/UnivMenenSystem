# Generated by Django 3.1.7 on 2021-05-25 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_student_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='specialty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.specialty'),
            preserve_default=False,
        ),
    ]
