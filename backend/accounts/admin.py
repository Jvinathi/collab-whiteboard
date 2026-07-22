
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Collaboration Settings', {'fields': ('avatar_color',)}),
    )


admin.site.register(User, CustomUserAdmin)