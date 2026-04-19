from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from . import models
from .serializers import *


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def register_api(request):
    data = request.data
    serializer = RegisterSerializer(data=data)

    if not serializer.is_valid():
        return Response({
            'status': '400', 
            'message': 'Error while creating user, please try again.', 
            'errors': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    print(serializer.data)
    return Response({
        'status': '201', 
        'message': 'User created successfully'
        }, 
        status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_api(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if not serializer.is_valid():
        print(data, "Data but it is not valid")
        return Response({
            'status': '400', 
            'message': 'Invalid login credentials.', 
            'errors': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST)

    #We will use validated_data since data has been validated and we are using custom DB, not built-in
    #So as a result, authenticate() method cannot be used here
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    #Filter the database value using username
    user = Reg_Users.objects.filter(username=username).first()

    print(user, "The current user")

    #If either user does not exist or user's password does not match
    #check_password(encoded password, original password)
    if not user or not check_password(password, user.password):
        return Response({
            'status': '401', 
            'message': 'Authentication failed. Please check your username and password.'
            }, 
            status=status.HTTP_401_UNAUTHORIZED)

    token = f"{user.id}_{user.username}_{user.password}"
    print(token)

    return Response({
        'status': '200', 
        'message': 'Login successful.',
        'token': token
        }, 
        status=status.HTTP_200_OK)