from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from main.models import ProfileModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages


def login_redirection(request):
    return redirect("authentication:login")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    error_message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                error_message = "User Not Found"
    else:
        form = LoginForm()

    context = {
        "error":error_message,
        "title":"Login",
        "forms":form
    }
    return render(
        request,
        "authentication/login.html",
        context
    )

@login_required(login_url="authentication:login")
def logout_page(request):
    return render(
        request,
        "authentication/logout.html"
    )

@login_required(login_url="authentication:login")
def logout_process(request):
    logout(request)
    return redirect("main:home")

def register(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            get_group = Group.objects.get(name="CommonUser")
            user = form.save()
            get_username = form.cleaned_data["username"]
            user.groups.add(get_group)
            ProfileModel.objects.create(
                user=user,
                name=get_username
            )
            messages.success(request, f"{get_username}'s Account Created!")
            return redirect("authentication:login")
    else:
        form = RegisterForm()
    
    context = {
        "title": "Register",
        "forms": form
    }
    return render(request, "authentication/register.html", context)