from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')


admin.site.register(User, UserAdmin)
