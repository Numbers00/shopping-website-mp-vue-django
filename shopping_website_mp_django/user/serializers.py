from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):   
    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "email",
            "address",
            "phone",
            "password"
        )