from import_export import resources
from .models import Visitor,Visit
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

class VisitorResource(resources.ModelResource):
    class Meta:
        model = Visitor

class VisitResource(resources.ModelResource):
    cellphone = Field(
        column_name='cellphone',
        attribute='cellphone',
        widget=ForeignKeyWidget(Visitor, 'cellphone'))

    class Meta:
        model = Visit
        use_bulk = True
