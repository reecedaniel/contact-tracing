from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('',views.LocationList.as_view(),name='locations'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='change_password')
    # path('location/new/',views.CreateLocation.as_view(),name='create')
]
