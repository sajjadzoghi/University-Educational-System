from rest_framework import mixins, generics, permissions, status

from environment_education.models import StudentLessons, ClassDayTime, LessonTeacher, DayTime

from environment_education.api.serializers import StudentLessonsSerializer, ClassDayTimeSerializer, \
    LessonTeacherSerializer, DayTimeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class IsSame(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user

    def has_permission(self, request, view):
        return request.user.is_authenticated


class LessonChoiceAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = StudentLessons.objects.all()
    serializer_class = StudentLessonsSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_permissions(self):
        permission_classes = [IsSame]
        return [permission() for permission in permission_classes]


class ClassDayTimeAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ClassDayTime.objects.all()
    serializer_class = ClassDayTimeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClassdtAPIView(APIView):

    def get_object(self, pk):
        try:
            return ClassDayTime.objects.get(id=pk)
        except ClassDayTime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        classDT = self.get_object(pk)
        res = ClassDayTimeSerializer(classDT, many=False).data
        return Response(res)

    def delete(self, request, pk, format=None):
        classDT = self.get_object(pk)
        classDT.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassdtListAPIView(APIView):

    def get_object(self, pk):
        try:
            return ClassDayTime.objects.filter(day_time__id=pk)
        except ClassDayTime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        classDTs = self.get_object(pk)
        res = ClassDayTimeSerializer(classDTs, many=True).data
        return Response(res)

    def delete(self, request, pk, format=None):
        classDTs = self.get_object(pk)
        classDTs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DayTimeAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = DayTime.objects.all()
    serializer_class = DayTimeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LessonTeacherAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = LessonTeacher.objects.all()
    serializer_class = LessonTeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
