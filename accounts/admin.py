from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from locations.models import Location

# Register your models here.
class LocationsInline(admin.TabularInline):
    model = Location

class UserProfileInline(admin.StackedInline):
    model = Profile

class NewUserAdmin(UserAdmin):
    inlines = [
        LocationsInline,
        UserProfileInline,
    ]

admin.site.unregister(User)
admin.site.register(User,NewUserAdmin)
admin.site.register(Profile)
