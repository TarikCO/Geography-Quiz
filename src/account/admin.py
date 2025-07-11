#Import of Django libraries
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account 

#Customizes the Django Admin interface for the Account Model
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#The Account model is registered in the Django Admin site.
admin.site.register(Account, AccountAdmin)


