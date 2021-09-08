from django.urls import path

from environment_education.api import views

urlpatterns = [
    path('generic/', views.LessonChoiceAPIView.as_view(), name='generic_lesson_choice')
]