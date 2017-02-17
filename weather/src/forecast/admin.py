from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WeatherForecast, User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_form_template = 'admin/change_form.html'


admin.site.register(User, CustomUserAdmin)
admin.site.register(WeatherForecast)
