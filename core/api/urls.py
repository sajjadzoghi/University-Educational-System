from django.urls import path, include

urlpatterns = [
    path('environment_education/', include('environment_education.api.urls')),
    path('persons/', include('persons.api.urls')),
]
