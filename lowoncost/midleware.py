import functools
from flask import session, redirect
def auth (view_func):
    @functools.wraps(view_func)
    def decorator(*arg, **kwargs):
        if "username" in session:
            username = session["username"]
            return redirect(f"/home/{username}")
        return view_func(*arg, **kwargs)
    return decorator

