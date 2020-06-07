from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import LoginPostForm


def index(request):
    if request.method == "POST":
        post_form = LoginPostForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            pd = post_form.cleaned_data['pd']
            user1 = authenticate(username=username, password=pd)
            if user1 is not None:
                auth.login(request, user1)
                post_form = LoginPostForm()
                return redirect('/')
            else:
                message = '登入失敗!'
        else:
            message = '驗證碼錯誤'
    else:
        message = '帳號,密碼及驗證碼都必須輸入!'
        post_form = LoginPostForm()
    return render(request, "index.html", locals())
