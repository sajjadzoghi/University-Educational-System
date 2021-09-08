from django.urls import path

from persons.api import views

urlpatterns = [
    path('teachers-list', views.teachers_list, name='teachers_list'),
    path('students-list/', views.students_list, name='students_list'),

]
