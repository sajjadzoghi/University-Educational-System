from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import ClassDayTime, College, StudentProfile, TeacherProfile
from .forms import RegStdForm, LessonChoiceForm, LoginForm, RegTeacherForm
from persons.models import User


# Create your views here.


class CollegeListView(generic.ListView):
    template_name = 'environment_education/colleges.html'
    context_object_name = 'colleges'

    def get_queryset(self):
        return College.objects.all()


class ClassListView(generic.ListView):
    template_name = 'environment_education/class-list.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        return ClassDayTime.objects.filter(college_id=self.kwargs['college_id'])


class ClassDetailView(generic.DetailView):
    model = ClassDayTime
    template_name = 'environment_education/class-details.html'


def reg_or_edit_student(request):
    if request.user.is_authenticated:
        student_form = RegStdForm(instance=get_object_or_404(StudentProfile, id=request.user.id))
    else:
        student_form = RegStdForm()
    if request.method == 'POST':
        student_form = RegStdForm(request.POST, request.FILES)
        if student_form.is_valid():
            std_name = f"{student_form.cleaned_data['first_name']} {student_form.cleaned_data['last_name']}"
            student_form.save()
            return render(request, 'environment_education/reg-success.html', context={'name': std_name, })
    return render(request, 'environment_education/reg-student.html', context={'student_form': student_form})


def reg_or_edit_teacher(request):
    if request.user.is_authenticated:
        teacher_form = RegTeacherForm(instance=get_object_or_404(TeacherProfile, id=request.user.id))
    else:
        teacher_form = RegTeacherForm()
    if request.method == 'POST':
        teacher_form = RegTeacherForm(request.POST, request.FILES)
        if teacher_form.is_valid():
            teacher_name = f"{teacher_form.cleaned_data['first_name']} {teacher_form.cleaned_data['last_name']}"
            teacher_form.save()
            return render(request, 'environment_education/reg-success.html', context={'name': teacher_name, })
    return render(request, 'environment_education/reg-teacher.html', context={'teacher_form': teacher_form, })


def lesson_choice(request):
    choice_forms = formset_factory(LessonChoiceForm, max_num=25, extra=4)
    if request.method == 'POST':
        std = StudentProfile.objects.get(personal_id=request.POST['std-id'])

        choice_forms = choice_forms(request.POST)
        if choice_forms.is_valid():
            for choice in choice_forms:
                choice = choice.save(commit=False)
                choice.student = std
                choice.save()
            return HttpResponse('Question has been submitted successfully')

    return render(request, 'environment_education/lesson-choice.html', context={
        'choice_forms': choice_forms,
    })


def library(request):
    choice_forms = formset_factory(LessonChoiceForm, max_num=25, extra=4)
    if request.method == 'POST':
        std = StudentProfile.objects.get(personal_id=request.POST['std-id'])

        choice_forms = choice_forms(request.POST)
        if choice_forms.is_valid():
            for choice in choice_forms:
                choice = choice.save(commit=False)
                choice.student = std
                choice.save()
            return HttpResponse('Books has been rented successfully!')

    return render(request, 'environment_education/library.html', context={
        'choice_forms': choice_forms,
    })


def login_view(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login(request, User.objects.get(mobile=login_form.cleaned_data['mobile']))
            if 'next' in request.GET:
                HttpResponseRedirect(request.GET['next'])
            return redirect('environment_education:colleges')

    return render(request, 'environment_education/login.html', context={
        'login_form': login_form
    })


def logout_view(request):
    logout(request)
    return redirect('environment_education:colleges')
