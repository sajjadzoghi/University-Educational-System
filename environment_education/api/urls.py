from django.urls import path

from environment_education.api import views

urlpatterns = [
    path('generic/', views.LessonChoiceAPIView.as_view(), name='generic_lesson_choice'),
    path('class-daytime/', views.ClassDayTimeAPIView.as_view(), name='generic_class_daytime'),
    path('class-daytime/<int:pk>', views.ClassdtAPIView.as_view(), name='classdt-detail'),
    path('classdt-list/<int:pk>', views.ClassdtListAPIView.as_view(), name='classdt-list'),
    path('daytime/', views.DayTimeAPIView.as_view(), name='generic_daytime'),
    path('lt/', views.LessonTeacherAPIView.as_view(), name='generic_lt')
]
