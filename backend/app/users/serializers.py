from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "location",
            "first_name",
            "last_name",
            "profile_picture",
            "profile_description",
            "current_position",
            "medical_ID",
            "medical_field",
        ]
        read_only_fields = ["email"]
