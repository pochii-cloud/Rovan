from django.urls import path

from accounts.views import *

urlpatterns = [
    path('LoginPageView/', LoginPageView.as_view(), name='LoginPageView'),
    path('RegisterView/', RegisterView.as_view(), name='RegisterView'),
    path('LogoutView/', LogoutView.as_view(), name='LogoutView'),
    path('ForgotPasswordView/', ForgotPasswordView.as_view(), name='ForgotPasswordView'),
    path('ForgotPasswordView/', ForgotPasswordView.as_view(), name='ForgotPasswordView'),
    path('ProfilePage/', ProfilePage.as_view(), name='ProfilePage'),
]
