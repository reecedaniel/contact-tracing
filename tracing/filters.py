from .models import Visit
import django_filters

class VisitFilter(django_filters.FilterSet):
    class Meta:
        model=Visit
        fields=['cellphone','timestamp']
