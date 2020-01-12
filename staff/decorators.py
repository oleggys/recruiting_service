from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def only_for(user_type, redirect_url, **redirect_url_args):
    def decorator(view):
        def inner(request, *args, **kwargs):
            if request.session.get('user_type') is None or request.session['user_type'] != user_type:
                if redirect_url is not None:
                    return redirect(redirect_url, **redirect_url_args)
                else:
                    raise PermissionDenied
            return view(request, *args, **kwargs)
        return inner
    return decorator

