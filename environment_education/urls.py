from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

app_name = 'environment_education'

urlpatterns = [
    path('', views.CollegeListView.as_view(), name='colleges'),
    path('<int:college_id>/class-list/', views.ClassListView.as_view(), name='class_list'),
    path('class-list/<int:pk>/', login_required(views.ClassDetailView.as_view()), name='class_detail'),
    path('register-student/', views.reg_or_edit_student, name='reg_std'),
    path('register-teacher/', views.reg_or_edit_teacher, name='reg_teacher'),
    path('edit-student-profile/<int:personal_id>/', views.reg_or_edit_student, name='edit_std'),
    path('edit-student-profile/<int:personal_id>/', views.reg_or_edit_teacher, name='edit_teacher'),
    path('lesson-choice/', views.lesson_choice, name='lesson_choice'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
