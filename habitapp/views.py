from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import HabitModel


def topfunc(request):
    return render(request, 'habitapp/top.html')


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
            return render(request, 'habitapp/top.html')
        except IntegrityError:
            return render(
                request,
                'habitapp/signup.html',
                {'error': 'このユーザーはすでに登録されています。'}
            )
    return render(request, 'habitapp/signup.html')


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 認証成功
            login(request, user)
            return redirect('habitapp:dashboard')
        else:
            # 認証失敗
            return render(
                request,
                'habitapp/login.html',
                {'context': 'ユーザーネームもしくはパスワードが間違っています。'}
            )
    return render(request, 'habitapp/login.html')


def logoutfunc(request):
    logout(request)
    return redirect('habitapp:top')


@login_required
def dashboardfunc(request):
    object_list = HabitModel.objects.all()
    good_list = HabitModel.objects.filter(good_or_bad__contains='good')
    bad_list = HabitModel.objects.filter(good_or_bad__contains='bad')
    return render(
        request,
        'habitapp/dashboard.html',
        {'object_list': object_list, 'good_list': good_list, 'bad_list': bad_list}
    )


def detailfunc(request, pk):
    object = get_object_or_404(HabitModel, pk=pk)
    return render(request, 'habitapp/detail.html', {'object': object})


class HabitCreate(generic.CreateView):
    model = HabitModel
    template_name = 'habitapp/create.html'
    fields = (
        'username',
        'habit',
        'frequency',
        'time_value',
        'time_unit',
        'good_or_bad'
    )
    success_url = reverse_lazy('habitapp:dashboard')


class HabitDelete(generic.DeleteView):
    model = HabitModel
    template_name = 'habitapp/delete.html'
    success_url = reverse_lazy('habitapp:dashboard')


class HabitUpdate(generic.UpdateView):
    model = HabitModel
    template_name = 'habitapp/update.html'
    fields = (
        'habit',
        'frequency',
        'time_value',
        'time_unit',
        'good_or_bad'
    )
    success_url = reverse_lazy('habitapp:dashboard')
