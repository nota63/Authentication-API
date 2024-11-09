from rest_framework import serializers

from .models import CustomUser


# serializer class
from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser  # Use your custom user model here
        fields = ['email', 'password', 'name']

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or not re.search(r'\d', value) or not re.search(r'[!@#$%^&*(),.?\":{}|<>]', value):
            raise serializers.ValidationError("Password must be at least 8 characters long, contain a number, and a special character.")
        return value

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    # serializer to validate email password, and issue a jwt token if the credentials are correct

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken






# create serializer to display profile details 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('id','email','name')


# serializer to handle the login validation and token generation

from rest_framework_simplejwt.tokens import RefreshToken
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
# create serializer for password reset

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator


User=get_user_model()

class PasswordResetRequestSerializer(serializers.Serializer):
    email=serializers.EmailField()

    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email")
        return value
    
    def save(self):
        email=self.validated_data['email']
        user=User.objects.get(email=email)
        token=PasswordResetTokenGenerator().make_token(user)
        uid=urlsafe_base64_encode(force_bytes(user.pk))
        return uid, token
    
# password reset confirm serializer 
from django.utils.http import urlsafe_base64_decode
class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    uid = serializers.CharField()
    token = serializers.CharField()

    def validate(self, data):
        try:
            # Decode the UID and retrieve the corresponding user
            uid = urlsafe_base64_decode(data['uid']).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError('Invalid token or user ID')

        # Validate the token for the user
        if not PasswordResetTokenGenerator().check_token(user, data['token']):
            raise serializers.ValidationError('Invalid or expired token')

        # Store the user instance in validated data so it can be accessed later in save()
        data['user'] = user
        return data

    def save(self, validated_data):
        # Now, retrieve the user instance from validated_data
        user = validated_data.get('user')
        if user:
            # Set the new password for the user
            user.set_password(validated_data['password'])
            user.save()  # Save the updated user instance
        return user
