from datetime import date
from random import randint
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from .managers import CustomUserManager


def generateTeacherPersonalId():
    today = date.today()
    generated = randint(int(str(today.year) + "0001"), int(str(today.year) + "9999"))
    if TeacherProfile.objects.filter(personal_id=generated).count() == 0:
        return generated
    else:
        generateTeacherPersonalId()


def generateStudentPersonalId():
    today = date.today()
    generated = randint(int(str(today.year) + "0001"), int(str(today.year) + "9999"))
    if StudentProfile.objects.filter(personal_id=generated).count() == 0:
        return generated
    else:
        generateStudentPersonalId()


# class StudentProfile(AbstractUser):
#     gender_choice = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     personal_id = models.IntegerField(unique=True, default=generateStudentPersonalId)
#     # personal_id = models.EmailField(_('Student ID'), unique=True, default=generateStudentPersonalId)
#     college = models.ForeignKey('environment_education.College', on_delete=models.CASCADE)
#     field = models.CharField(max_length=200)
#     birthdate = models.DateField(blank=True, null=True)
#     mobile = models.IntegerField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     photo = models.ImageField(upload_to='students/%Y/%m/%d', blank=True, null=True)
#     gender = models.CharField(max_length=10, choices=gender_choice, default='Male', blank=True, null=True)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return f'{self.username}, {self.first_name, self.last_name}'



class StudentProfile(models.Model):
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_id = models.IntegerField(unique=True, default=generateStudentPersonalId)
    college = models.ForeignKey('environment_education.College', on_delete=models.CASCADE)
    field = models.CharField(max_length=200)
    birthdate = models.DateField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='students/%Y/%m/%d', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choice, default='Male', blank=True, null=True)
#
#     class Meta:
#         verbose_name_plural = 'Students'
#         verbose_name = 'Student'
#
#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_id = models.IntegerField(unique=True, default=generateTeacherPersonalId)
    college = models.ForeignKey('environment_education.College', on_delete=models.CASCADE)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='teachers/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Teachers'
        verbose_name = 'Teacher'

    # def __str__(self):
        # return f'{self.user.first_name} {self.user.last_name}'
