from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.contrib import messages

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'دسترسی غیرمجاز')
                return redirect('homepage:home')
        return _wrapped_view
    return decorator

def roles_required(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'دسترسی غیرمجاز')
                return redirect('homepage:home')
        return _wrapped_view
    return decorator
