from .models import Recipe,Review
from rest_framework import serializers
from django.contrib.auth.models import User

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_user):
        u=User.objects.create_user(username=validated_user['username'],password=validated_user['password'])
        u.save()
        return u

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields= '__all__'
