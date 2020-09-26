from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # List of http status codes we can use to return things from our API

from profiles_api import serializers # tells APIView what to expect for Post, Put and Patch

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
        
