from django.shortcuts import redirect

def authenticate_redirection(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        return redirect("authentication:login")

def admin_page(request):
    if request.user.is_superuser:
        return redirect("/admin/")
    else:
        return redirect("main:home")