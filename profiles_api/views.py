from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # List of http status codes we can use to return things from our API
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers # tells APIView what to expect for Post, Put and Patch
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP method as function (get,post,patch,put,delete)',
        'Is similar to a traditional django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our Name"""
        serializer = self.serializer_class(data=request.data) #This is how we Retrive a serializer class in an APIView

        if serializer.is_valid():
            name = serializer.validated_data.get('name') # Retrives the Name field.
            message = f'Hello {name}' # the f'' method inserts the name into the string
            return Response({'message':message})
        else:
             return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST #We can also pass just 400 but this is a better way for doc purposes
                )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'}) #Replaces an object

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'}) # Updates only specific parts of the object.

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list,create,Retrive,update,partial_update,delete)',
            'automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

        def retrive(self,request,pk=None):
            """Handle getting an object by its ID"""
            return Response({'http_method':'GET'})

        def update(self,request,pk=None):
            """Handle updating an object"""
            return Response({'http_method':'PUT'})

        def partial_update(self,request,pk=None):
            """Handle updating part of an object"""
            return Response({'http_method':'PATCH'})

        def destroy(self,request,pk=None):
            """Handle removing an object"""
            return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # authenticates every request
    permission_classes = (permissions.UpdateOwnProfile,) # checks each user's permissions
    filter_backends = (filters.SearchFilter,)#that comma is just to tell python that this is a tuple
    search_fields = ('name','email',)
