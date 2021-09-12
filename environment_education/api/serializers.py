from rest_framework import serializers

from environment_education.models import DayTime, College, LessonTeacher, ClassDayTime, LessonClass, \
    StudentLessons



class CollegeSerializer(serializers.ModelSerializer):
    # student = serializers.SerializerMethodField('get_student_id')
    class Meta:
        model = College
        fields = '__all__'



class LessonTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTeacher
        fields = '__all__'
        depth = 1


class ClassDayTimeSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(many=False)
    day_time = DayTimeSerializer(many=False)

    class Meta:
        model = ClassDayTime
        fields = '__all__'


class DayTimeSerializer(serializers.ModelSerializer):
    classes = ClassDayTimeSerializer(many=True)


    class Meta:
        model = DayTime
        fields = '__all__'


class LessonClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonClass
        fields = '__all__'


class StudentLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLessons
        fields = '__all__'
