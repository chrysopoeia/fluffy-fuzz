from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminCustom(UserAdmin):
    list_display = ('email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_form_template = 'admin/change_form.html'


admin.site.register(User, UserAdminCustom)
