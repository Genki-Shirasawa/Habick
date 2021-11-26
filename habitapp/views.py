from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import HabitModel


def topfunc(request):
    return render(request, 'top.html')


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
            return render(request, 'top.html')
        except IntegrityError:
            return render(
                request,
                'signup.html',
                {'error': 'このユーザーはすでに登録されています。'}
            )
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 認証成功
            login(request, user)
            return redirect('dashboard')
        else:
            # 認証失敗
            return render(
                request,
                'login.html',
                {'context': 'ユーザーネームもしくはパスワードが間違っています。'}
            )
    return render(request, 'login.html')


def logoutfunc(request):
    logout(request)
    return redirect('top')


@login_required
def dashboardfunc(request):
    object_list = HabitModel.objects.all()
    good_list = HabitModel.objects.filter(good_or_bad__contains='good')
    bad_list = HabitModel.objects.filter(good_or_bad__contains='bad')
    return render(
        request,
        'dashboard.html',
        {'object_list': object_list, 'good_list': good_list, 'bad_list': bad_list}
    )


def detailfunc(request, pk):
    object = get_object_or_404(HabitModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


class HabitCreate(CreateView):
    template_name = 'create.html'
    model = HabitModel
    fields = (
        'username',
        'habit',
        'frequency',
        'time_value',
        'time_unit',
        'good_or_bad'
    )
    success_url = reverse_lazy('dashboard')


class HabitDelete(DeleteView):
    template_name = 'delete.html'
    model = HabitModel
    success_url = reverse_lazy('dashboard')


class HabitUpdate(UpdateView):
    template_name = 'update.html'
    model = HabitModel
    fields = (
        'habit',
        'frequency',
        'time_value',
        'time_unit',
        'good_or_bad'
    )
    success_url = reverse_lazy('dashboard')
