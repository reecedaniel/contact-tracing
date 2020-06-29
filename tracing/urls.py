from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'tracing'

urlpatterns = [
    path('<int:pk>/',views.VisitLog,name='visit'),
    path('post/ajax/',views.formSubmit,name='post_visitor'),
    path('get/ajax/',views.checkCell,name='check_cell'),
    path('visitorlist/',views.VisitorListView.as_view(),name='visitor_list'),
    path('',views.VisitListView.as_view(),name='visits'),
]
