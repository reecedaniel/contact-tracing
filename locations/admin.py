from django.contrib import admin
from .models import Location
from tracing.models import Visitor,Visit
# Register your models here.
class VisitsInline(admin.TabularInline):
    model = Visit
    readonly_fields = ('cellphone','timestamp')

class NewVisitorAdmin(admin.ModelAdmin):
    inlines = [
        VisitsInline,
    ]

admin.site.register(Location,NewVisitorAdmin)
