from django.http import HttpResponse
from django.urls import reverse

def allowed_role(roles=[]):
    def decorator(func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0]
            if str(group) in roles or request.user.is_superuser:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    "<h1>You are not allowed to access this page</h1> <br> <a href='" + reverse('main:profile') + "' class='btn btn-warning'>Back</a>"
                )
        return wrapper_func
    return decorator