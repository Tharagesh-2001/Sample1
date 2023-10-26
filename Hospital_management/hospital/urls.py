from django.urls import path, include
from .views import DoctorRegisterView, DoctorLoginView, DoctorLogoutView, DoctorProfileView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('doctor/register/', DoctorRegisterView.as_view(), name='doctor-register'),
    path('doctor/login/', DoctorLoginView.as_view(), name='doctor-login'),
    path('doctor/logout/', DoctorLogoutView.as_view(), name='doctor-logout'),
    path('doctor/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('doctor/profile/', DoctorProfileView.as_view(), name='doctor-profile'),
]