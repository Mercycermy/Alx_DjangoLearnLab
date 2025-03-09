from rest_framework import serializers
from .models import Book
from django.contrib.auth import get_user_model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =  '_all_'

        
User = get_user_model()  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for the available users in this project"""
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'groups']