from django.urls import path,include
from . import views
from tracing import views as tracing_views

app_name = 'locations'

urlpatterns = [
    path('',views.LocationList.as_view(),name='locations'),
    # path('<int:pk>/',include("tracing.urls",namespace="tracing")),
    path('new/',views.CreateLocation.as_view(),name='create'),
    path('info/<int:pk>/',views.LocationDetailView.as_view(),name='detail'),
]
