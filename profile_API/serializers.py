from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model





class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)




class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=get_user_model().objects.all())
        ]
    )

    class Meta:
        model = User
        fields = ('id','email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user