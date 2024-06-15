from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_admin')
    search_fields = ('email', 'name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'services')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'services'),
        }),
    )

    list_filter = ('is_admin', 'is_active')

    filter_horizontal = ()

admin.site.register(User, UserAdmin)
