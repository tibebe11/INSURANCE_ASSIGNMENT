from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from functools import wraps

def custom_user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and not u.is_anonymous and not u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def superuser_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and not u.is_anonymous and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator