from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegistrationView, SuccessRegistrationView, ActivationView, SigninView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('successfull_registration/', SuccessRegistrationView.as_view(), name="successfull-registration"),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
