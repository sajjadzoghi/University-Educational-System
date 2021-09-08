from django.db import models
from persons.models import TeacherProfile, StudentProfile


# Create your models here.
class DayTime(models.Model):
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ['day', 'start_time', 'end_time']

    def __str__(self):
        return f'{self.day} {self.start_time}-{self.end_time}'

    @property
    def get_day_time(self):
        return f'{self.day}, {self.start_time}-{self.end_time}'


class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonTeacher(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='lesson_teachers')
    lesson = models.CharField(max_length=100)
    units_number = models.IntegerField()
    capacity = models.PositiveSmallIntegerField()
    exam_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'lesson:{self.lesson}, teacher:{self.teacher}, {self.capacity}'


class ClassDayTime(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='classes')
    class_num = models.PositiveSmallIntegerField()
    day_time = models.ForeignKey(DayTime, on_delete=models.CASCADE, related_name='classes')

    class Meta:
        unique_together = [['college', 'class_num', 'day_time']]

    def __str__(self):
        return f'class{self.class_num}, {self.day_time}'


class LessonClass(models.Model):
    class_daytime = models.OneToOneField(ClassDayTime, on_delete=models.CASCADE)
    lesson_teacher = models.ForeignKey(LessonTeacher, on_delete=models.CASCADE, related_name='lesson_classes')

    class Meta:
        unique_together = [['class_daytime', 'lesson_teacher']]

    def __str__(self):
        return f'{self.lesson_teacher}, {self.class_daytime}'


class StudentLessons(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_lessons')
    lesson_class = models.ForeignKey(LessonClass, on_delete=models.CASCADE, related_name='student_lessons')

    def __str__(self):
        return self.lesson_class