from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import LessonClass, StudentLessons
from persons.models import StudentProfile, TeacherProfile


# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class RegStdForm(UserCreationForm):
#     class Meta:
#         model = StudentProfile
#         fields = ('first_name', 'last_name', 'username', 'personal_id', 'password1', 'password2', 'college', 'field')
#
#
# class EditStdForm(UserChangeForm):
#     class Meta:
#         model = StudentProfile
#         fields = ('first_name', 'last_name', 'username', 'personal_id', 'password1', 'password2', 'college', 'field')


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class RegStdForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['college', 'field', 'personal_id', ]


class RegTeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['college', 'personal_id', ]

    # def save(self, **kwargs):
    #     teacher = super().save(commit=False)
    #     user = User.objects.create(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'],
    #                                last_name=self.cleaned_data['last_name'], email=self.cleaned_data['email'])
    #     user.set_password(self.cleaned_data['password'])
    #     teacher.user = user
    #     teacher.save(commit=True)
    #     return teacher


class LessonChoiceForm(forms.ModelForm):
    class Meta:
        model = StudentLessons
        exclude = ['student', ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
