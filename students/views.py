from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import StudentForm, SubjectForm, SpecialtyForm, CreateUserForm, LoginForm
from .models import Specialty, Student, Subject
from django.db.models import Avg


def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request, 'students/register.html', context)


def loginPage(request):

	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'Authenticated successfully')
				return redirect('home')
			else:
				messages.error(request, 'Invalid login')
	else:
		form = LoginForm()

	context = {'form':form}

	return render(request, 'students/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
	students = Student.objects.all()
	
	average = 0
# avg = sum(number_list)/len(number_list)
	for student in students:
		subjects = Subject.objects.filter(student=student.id)
		
		lst = []
		for i in subjects:
			lst.append(i.mark)


		if len(lst) != 0:
			student.averageMark = round((sum(lst)/len(lst)), 1)
			student.save()	
		else:
			student.averageMark = 0
			student.save()


		if student.averageMark >= 4:
			student.status = True
			student.save()
		else:
			student.status = False
			student.save()


	
	context = {
		'students': students,
		'average': average,
	}

	return render(request, 'students/home.html', context)


def createStundent(request):
	form = StudentForm()

	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Student added successfully!')
			return redirect('/')
	context = {
		'form':form,
	}

	return render(request, 'students/createStudent.html', context)


def createSubject(request):
	form = SubjectForm()

	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Subject added successfully!')
			return redirect('/')
	context = {
		'form':form,
	}

	return render(request, 'students/createSubject.html', context)


def createSpecialty(request):
	form = SpecialtyForm()

	if request.method == 'POST':
		form = SpecialtyForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Specialty added successfully!')
			return redirect('specialtyList')
	context = {
		'form':form,
	}

	return render(request, 'students/createSpecialty.html', context)


def viewStudent(request, pk):
	student = Student.objects.get(id=pk)

	subjects = Subject.objects.filter(student = student.id)

	average = 0
	for i in subjects:
		average += i.mark
	
	if len(subjects) != 0:
		average = round((average/len(subjects)), 2)

	else:
		average = 0


	context = {
		'student': student,
		'subjects': subjects,
		'average': average,
	}

	return render(request, 'students/viewStudent.html', context)


def deleteStudent(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == "POST":
		student.delete()
		return redirect('/')

	context = {'item':student}
	return render(request, 'students/delete.html', context)


def updateSubject(request, pk):
	subject = Subject.objects.get(id=pk)
	form = SubjectForm(instance=subject)

	if request.method == 'POST':
		form = SubjectForm(request.POST, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'students/updateSubject.html', context)


def specialtyList(request):
    specialties = Specialty.objects.all()

    context = {
        'specialties': specialties,
    }

    return render(request, 'students/SpecialtyList.html', context)


def viewSpecialty(request, pk):
	specialty = Specialty.objects.get(id=pk)

	students = Student.objects.filter(specialty = specialty.id)
	context = {
		'students': students,
		'specialty': specialty,
	}

	return render(request, 'students/viewSpecialty.html', context)