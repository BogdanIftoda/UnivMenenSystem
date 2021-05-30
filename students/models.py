from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Specialty(models.Model):
    SpecialtyName = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.SpecialtyName


class Student(models.Model):

    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    middleName = models.CharField(max_length=50, null=False, blank=False)
    averageMark = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    status = models.BooleanField(default=False)
    birthDate = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    class Meta:
    	ordering = ('specialty',)

    def __str__(self):
        return f'{self.lastName} {self.firstName} {self.middleName}'


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjectName = models.CharField(max_length=100, null=False, blank=False)
    mark = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    created_at = models.DateTimeField(
      auto_now_add=True
    )

    def __str__(self):
        return self.subjectName

