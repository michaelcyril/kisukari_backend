from django.urls import path
from .views import *
app_name = 'user_management'

urlpatterns = [
    path('verify-phone', VerifyPhone.as_view()),
    path('verify-otp', VerifyOtp.as_view()),
]
