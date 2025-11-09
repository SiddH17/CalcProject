from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from . import models
from .serializers import *


from rest_framework.decorators import api_view
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
    return Response({
        'status': '201', 
        'message': 'User created successfully'
        }, 
        status=status.HTTP_201_CREATED)

