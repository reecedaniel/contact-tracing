from django.contrib import admin
from .models import Visitor,Visit

# Register your models here.
class AccessRecordsInline(admin.TabularInline):
    model = Visit

class AccessRecordAdmin(admin.ModelAdmin):
    inlines = [
        AccessRecordsInline,
    ]
    
admin.site.register(Visitor,AccessRecordAdmin)
admin.site.register(Visit)
