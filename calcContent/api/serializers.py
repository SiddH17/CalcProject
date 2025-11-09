from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

#Serializer for Register API call
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Users
        fields = '__all__'
    
    #Validation message for user registration
    def validate(self, data):
        if data['username']:
            #Throw a validation error if the user already exists in the system
            if Reg_Users.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError({'username': 'Username already exists.'})
            
        if data['email']:
            #Throw a validation error if email ID already exists in the system
            if Reg_Users.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError({'email': 'Email Address already exists.'})
            
        return data
    
    #Create the new user by saving their details
    def create(self, validated_data):
        #After validation, save the details
        user = Reg_Users.objects.create(
            name = validated_data['name'],
            username = validated_data['username'],
            email = validated_data['email']
            )
        validated_data['password'] = make_password(validated_data['password'])
        user.save()
        print(user)

        return user