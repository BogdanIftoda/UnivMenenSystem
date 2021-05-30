from django import forms
from .models import Student, Subject, Specialty
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lastName'].widget.attrs.update(placeholder='Enter last name...')
        self.fields['firstName'].widget.attrs.update(placeholder='Enter first name...')
        self.fields['middleName'].widget.attrs.update(placeholder='Enter middle name...')
        self.fields['birthDate'].widget.attrs.update(placeholder='y-m-d')

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['created_at', 'status', 'averageMark']


class SubjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mark'].widget.attrs.update(min='0', max='12', placeholder='Enter mark...')
        self.fields['subjectName'].widget.attrs.update(placeholder='Enter subject name...')

    class Meta:
        model = Subject
        fields = '__all__'
        exclude = ['created_at',]


class SpecialtyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['SpecialtyName'].widget.attrs.update(placeholder='Enter specialty...')

    class Meta:
        model = Specialty
        fields = '__all__'
