from rest_framework import serializers

from environment_education.models import DayTime, College, LessonTeacher, ClassDayTime, LessonClass, \
    StudentLessons


class DayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayTime
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField('get_student_id')
    class Meta:
        model = College
        fields = '__all__'

    def get_student_id(self):
        college = College.objects.get(id=self.id)



class LessonTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTeacher
        fields = '__all__'


class ClassDayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDayTime
        fields = '__all__'


class LessonClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonClass
        fields = '__all__'


class StudentLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLessons
        fields = '__all__'
