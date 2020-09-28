from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a UserProfile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')

        extra_kwargs = {   #kwargs means key word arguments
            'password': {
                'write_only':True,
                 'style': {'input_type': 'password'}
            }
        }
    def create(self,validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')# should not be able to create a new user profile through this.

        # We add Key word arguments to make sure new user profiles and created_on are not added by the user.
        extra_kwargs = {'user_profile': {'read_only': True}}
