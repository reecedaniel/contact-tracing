from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from locations.models import Location

# Register your models here.
class LocationsInline(admin.TabularInline):
    model = Location

class NewUserAdmin(UserAdmin):
    inlines = [
        LocationsInline,
    ]

admin.site.unregister(User)
admin.site.register(User,NewUserAdmin)
