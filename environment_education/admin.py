from django.contrib import admin, messages
from .models import DayTime, College, ClassDayTime, LessonTeacher, LessonClass, StudentLessons
from django.utils.translation import ngettext

admin.site.register(DayTime)
admin.site.register(StudentLessons)

# Register your models here.
class ClassDayTimeInline(admin.TabularInline):
    model = ClassDayTime
    extra = 2
    max_num = 50


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    inlines = [ClassDayTimeInline, ]


@admin.register(ClassDayTime)
class ClassDayTimeAdmin(admin.ModelAdmin):
    list_display = ['class_num', 'day_time' ]
    search_fields = ['class_num', ]


@admin.register(LessonTeacher)
class LessonTeacherAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'teacher']
    search_fields = ['lesson', ]


@admin.register(LessonClass)
class LessonClassAdmin(admin.ModelAdmin):
    list_display = ['lesson_teacher', 'class_daytime']
    search_fields = ['lesson_teacher', ]
#     @admin.action(description="تغییر وضعیت سفارش به  'دایر'")
#     def change_statusــcancel(self, request, queryset):
#         update = queryset.update(status=1)
#         self.message_user(request, ngettext(
#             '  %d مورد با موفقیت تغییر یافت', '  %d مورد با موفقیت تغییر یافتند',
#             update, ) % update, messages.SUCCESS)
#
#     @admin.action(description="تغییر وضعیت سفارش به  'تعطیل'")
#     def change_statusــcancel(self, request, queryset):
#         update = queryset.update(status=0)
#         self.message_user(request, ngettext(
#             '  %d مورد با موفقیت تغییر یافت', '  %d مورد با موفقیت تغییر یافتند',
#             update, ) % update, messages.SUCCESS)
