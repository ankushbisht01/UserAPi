from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters
from . import serializers 
from . import models
from . import permissions
from django.contrib.auth.models import User

# Create your views here.
class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    def get(self , request , format=None):

        an_apiview = [
            'use HTTP as function(get,post,patch , put , delete)',
            'It is similar to a traditional django view',
            'Gives you most control over your logic',
            'it mapped manually to the URLs'
        ]

        return Response({'message':'hello!','an_apiview':an_apiview})
    def post(self ,request):

        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello{0}'.format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request , pk=None):
        return Response({"method":"put"})

    def patch(self , request , pk =None):
        return Response({'method':'patch'})
    
    def delete(self , request , pk =None):
        return Response({'method':'delete'})


class HelloViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self,request):


        a_viewset = [
            "User action (list , create , patial_update , update, retrive )",
            "Automatically maps URLs through router",
            'a view set provide more functionality with less code'
        ]

        return Response({'message':"hello ","a_viewset":a_viewset})
    

    def create (self ,request):

        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello{0}'.format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self , request , pk=None):
        return Response({'Http_method':'GET'})


    def update(self , request , pk= None):
        return Response({'HTTP_method':'POST'})
    

    def partial_update(self , request , pk = None):
        return Response({'http_method':'PATCH'})

    def destroy(self , request , pk = None):
        return Response({'http_method':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
        serializer_class = serializers.UserProfileSerializer
        queryset = User.objects.all()
        authentication_classes = (TokenAuthentication,)
        permission_classes = (permissions.UpdateOwnProfile,)
        filter_backends = (filters.SearchFilter,)
        search_fields = ('username','email',)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    

    def create(self , request ):
        return (ObtainAuthToken().post(request))
        