from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MemberForm


def signup(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username, password=password)
            login(request, new_user)

            return redirect('/post/')
    else:
        form = MemberForm()

        context = {
            'form': form
        }

        return render(request, 'member/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/post/')
        else:
            return HttpResponse('로그인에 실패했습니다.')

    else:
        form = MemberForm()

        context = {
            'form': form
        }

    return render(request, 'member/signin.html', context)
