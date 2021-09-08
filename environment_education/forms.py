from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
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


# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email',)


class RegStdForm(UserCreationForm):
    class Meta:
        model = StudentProfile
        fields = ['personal_id', 'mobile', 'first_name', 'last_name', 'college', 'field', ]


class RegTeacherForm(UserCreationForm):
    class Meta:
        model = TeacherProfile
        fields = ['personal_id', 'mobile', 'first_name', 'last_name', 'college', ]

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
    mobile = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    type = forms.ChoiceField(choices=[
        ('student', 'student'),
        ('teacher', 'teacher'),
    ])

    def clean(self):
        cleaned_data = self.data
        user = authenticate(mobile=cleaned_data['mobile'], password=cleaned_data['password'])
        if user is None:
            raise forms.ValidationError("Sorry! User doesn't exist.")
        return cleaned_data
