# from environment_education.api.serializers import StudentLessonsSerializer
from rest_framework import mixins, generics, permissions

from environment_education.models import StudentLessons

from environment_education.api.serializers import StudentLessonsSerializer


class LessonChoiceAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = StudentLessons.objects.all()
    serializer_class = StudentLessonsSerializer
    permission_classes = [permissions.DjangoModelPermissions.has_permission()]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)