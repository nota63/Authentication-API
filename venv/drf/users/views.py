from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
# create views to handle user registration
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login view that will handle the jwt authentication and return jwt


from django_ratelimit.decorators import ratelimit
from .serializers import LoginSerializer



# Custom function to fetch IP from request data or use a default IP
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# retrive authenticated users data 
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

# # BONUS FEATURES 
# password reset view

from .serializers import PasswordResetRequestSerializer
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


class PasswordResetRequestView(APIView):
    def post(self,request):
        serializer=PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            uid, token=serializer.save()

            # construct reset url
            reset_link=request.build_absolute_uri(
                reverse('reset_confirm',kwargs={'uid':uid,"token":token})
            )

            # send the mail
            send_mail(
                subject='Password Reset Request',
                message=f'Click the link to reset your password: {reset_link}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[serializer.validated_data['email']]

            )
            return Response({'message':'password reset link sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# password reset confirm view

from .serializers import PasswordResetConfirmSerializer

class PasswordResetConfirmView(APIView):
    def post(self,request,uid,token):
        serializer=PasswordResetConfirmSerializer(data={**request.data,'uid':uid,'token':token})
        if serializer.is_valid():
            user=serializer.validated_data
            serializer.save(user)
            return Response({'message':'password has been reset successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
