from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appWatpool.models import Account
class Accountadmin(UserAdmin):
    list_display = ('email','last_login', 'is_active', 'is_admin', 'is_superuser')
    search_fields = ('email')
    readonly_fields = ('id','last_login')

    ordering = ('email','last_login', 'is_active', 'is_admin', 'is_superuser')
    search_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(Account, Accountadmin)

# Register your models here.
