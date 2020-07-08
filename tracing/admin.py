from django.contrib import admin
from .models import Visitor,Visit
from import_export.admin import ImportExportMixin,ImportExportModelAdmin
from .resources import VisitorResource,VisitResource
# Register your models here.
class AccessRecordsInline(admin.TabularInline):
    model = Visit

class AccessRecordAdmin(ImportExportMixin,admin.ModelAdmin):
    inlines = [
        AccessRecordsInline,
    ]
    resource_class = VisitorResource
    search_fields = ('name', 'cellphone')

class VisitAdmin(ImportExportModelAdmin):
    resource_class = VisitResource
    pass

admin.site.register(Visitor,AccessRecordAdmin)
admin.site.register(Visit,VisitAdmin)
