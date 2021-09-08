from rest_framework.decorators import api_view
from rest_framework.response import Response

from persons.api.serializers import TeacherProfileSerializer, StudentProfileSerializer
from persons.models import StudentProfile, TeacherProfile


@api_view(['GET', 'POST'])
def teachers_list(request):
    if request.method == 'GET':
        resp = dict()
        resp['teachers'] = TeacherProfileSerializer(TeacherProfile.objects.all(), many=True).data
        return Response(resp)


@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        resp = dict()
        resp['students'] = StudentProfileSerializer(StudentProfile.objects.all(), many=True).data
        return Response(resp)