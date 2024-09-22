from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileModel, ProductModel
from .forms import ProfileForm, ProductForm
from django.contrib.auth.models import Group, User
from . import decorator
from django.core.paginator import Paginator

def main_redirection(request):
    return redirect("main:home")

def check_role(request):
    if request.user.is_superuser:
        return "SuperUserNav.html"
    else:
        role = request.user.groups.all()[0]
        if str(role) == "Staff":
            return "StaffNav.html"
        else:
            return "CommonUserNav.html"

@login_required(login_url="authentication:login")
def home(request):
    get_role = check_role(request)
    paginator = Paginator(
        ProductModel.objects.all(),
        9
    )
    page = request.GET.get("page")
    get_products = paginator.get_page(page)
    context = {
        "title":"Home",
        "NavRole":get_role,
        "products":get_products,
        "products_amount":len(get_products)
    }
    return render(
        request,
        "main/home.html",
        context
    )


@decorator.allowed_role(["Staff"])
def create(request):
    get_role = check_role(request)
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.creator = request.user.username
            temp_form.save()
            return redirect("main:home")
    else:
        form = ProductForm()
    context = {
        "title":"Create",
        "NavRole":get_role,
        "forms":form
    }
    return render(
        request,
        "main/create.html",
        context
    )

@login_required(login_url="authentication:login")
def view_profile(request):
    get_role = check_role(request)
    get_profiles = ProfileModel.objects.get(
        user=request.user
    )
    if request.user.is_superuser:
        group = "SuperUser"
    else:
        group = request.user.groups.all()[0]

    context = {
        "title":"Profile",
        "NavRole":get_role,
        "profiles":get_profiles,
        "groups":group 
    }
    return render(
        request,
        "main/profile.html",
        context
    )

def edit_profile(request):
    get_role = check_role(request)
    get_data = ProfileModel.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            initial=get_data.__dict__,
            instance=get_data
        )
        if form.is_valid():
            form.save()
            return redirect("main:profile")
    else:
        form = ProfileForm(
            initial=get_data.__dict__,
            instance=get_data
        )

    context = {
        "title":"Edit Profile",
        "forms":form,
        "NavRole":get_role
    }
    return render(
        request,
        "main/edit_profile.html",
        context
    )

@decorator.allowed_role(["staff"])
def update_product(request, slug_product):
    get_role = check_role(request)
    get_target = ProductModel.objects.get(
        slug__iexact=slug_product
    )
    current_data = get_target.__dict__
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            initial=current_data,
            instance=get_target
        )
        if form.is_valid():
            form.save()
            return redirect("main:home")
    else:
        form = ProductForm(
            initial=current_data,
            instance=get_target
        )
    
    context = {
        "title":"Update Product",
        "forms":form,
        "NavRole":get_role
    }
    return render(
        request,
        "main/update_product.html",
        context
    )

def detail_product(request, slug_product):
    get_role = check_role(request)
    get_target = ProductModel.objects.filter(
        slug__iexact=slug_product
    )

    context = {
        "title":f"Product Detail",
        "products":get_target,
        "NavRole":get_role
    }
    return render(
        request,
        "main/detail_product.html",
        context
    )

@decorator.allowed_role(["staff"])
def delete_product(request, slug_product):
    get_target = ProductModel.objects.get(
        slug__iexact=slug_product
    )
    if request.method == "POST":
        get_target.delete()
        return redirect("main:home")
    
    context = {
        "title":"Delete Product",
        "product":get_target.name
    }
    return render(
        request,
        "main/delete_product.html",
        context
    )