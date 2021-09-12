from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import TeacherProfile, StudentProfile

# admin.site.register(TeacherProfile)
# admin.site.register(StudentProfile)


# class StudentProfileInline(admin.StackedInline):
#     model = StudentProfile
#     can_delete = False
#     verbose_name_plural = 'student'


#
#
# class TeacherProfileInline(admin.StackedInline):
#     model = TeacherProfile
#     can_delete = False
#     verbose_name_plural = 'teacher'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (StudentProfileInline,)
#
#
# admin.site.unregister(User)
admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)

# Register your models here.
# class LessonInline(admin.StackedInline):
#     model = Lesson
#     extra = 0
#     max_num = 5
# class ProfessorInline(admin.StackedInline):
#     model = Professor
#     extra = 0
#     max_num = 5


# inlines = [ProfessorInline,]

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['mobile', ]
#     fields = ['user','date_of_entery',]
#     search_fields = ['mobile', 'lessons']
#     # inlines = [LessonInline,]
#
# @admin.register(Professor)
# class ProfessorAdmin(admin.ModelAdmin):
#     list_display = ['mobile', ]
#     fields = ['user','mobile',]
#     search_fields = ['mobile', ]
