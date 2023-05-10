
from rest_framework import serializers
from .models import Account


        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["email", "password"]

    def create(self, validated_data):
        user = Account.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user