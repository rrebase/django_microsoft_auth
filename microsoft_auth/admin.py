from django.apps import apps
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MicrosoftAccount

User = get_user_model()

# override admin site template
admin.site.login_template = "microsoft/admin_login.html"

# djangoql support
extra_base = []
if apps.is_installed("djangoql"):  # pragma: no branch
    from djangoql.admin import DjangoQLSearchMixin  # pragma: no cover

    extra_base = [DjangoQLSearchMixin]  # pragma: no cover

base_admin = extra_base + [admin.ModelAdmin]
base_user_admin = extra_base + [BaseUserAdmin]

# unregister User mode if it is already registered
if admin.site.is_registered(User):  # pragma: no branch
    admin.site.unregister(User)


@admin.register(MicrosoftAccount)
class MicrosoftAccountAdmin(*base_admin):
    readonly_fields = ("microsoft_id",)
