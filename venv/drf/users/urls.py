from django.urls import path, include
from .views import UserRegistrationView,LoginView,UserProfileView, PasswordResetRequestView, PasswordResetConfirmView

urlpatterns=[
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('reset_request/',PasswordResetRequestView.as_view(), name='reset_request'),
    path('reset_confirm/<str:uid>/<str:token>/', PasswordResetConfirmView.as_view(), name='reset_confirm')

]