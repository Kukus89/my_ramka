from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


@admin.register(MyUser)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
    )

    list_editable = (
        "first_name",
        "last_name",
        "email"
    )


UserAdmin.fieldsets += (
    ('Биография', {'fields': ('bio',)}),
)
# admin.site.register(MyUser, UserAdmin)
