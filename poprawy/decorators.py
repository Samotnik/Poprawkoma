from django.http import HttpResponse
from django.shortcuts import redirect

def unaauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == allowed_roles:
                return view_func(request, *args,**kwargs)
            else:
                return redirect('nauczyciel_page')
        return wrapper_func
    return decorator