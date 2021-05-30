from django.urls import path
from .views import createStundent, createSubject, createSpecialty, deleteStudent, home, viewStudent, registerPage, loginPage, logoutUser, updateSubject, specialtyList, viewSpecialty



urlpatterns = [

	path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),



    path('', home, name='home'),
    path('createStudent', createStundent, name='createStudent'),
    path('createSubject', createSubject, name='createSubject'),
    path('createSpecialty', createSpecialty, name='createSpecialty'),
    path('viewStudent/<int:pk>', viewStudent, name='viewStudent'),
    path('deleteStudent/<int:pk>', deleteStudent, name="deleteStudent"),
    path('updateSubject/<int:pk>', updateSubject, name='updateSubject'),
    path('specialtyList', specialtyList, name='specialtyList'),
    path('viewSpecialty/<int:pk>', viewSpecialty, name='viewSpecialty'),
]