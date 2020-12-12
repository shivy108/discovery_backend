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
            # "location",
            # "first_name",
            # "last_name",
            # "avatar",
            # "medical_id",
            # "medical_field",
            # "about_me",
            # "banner",
            # "liked_posts",
            # "followees",
        ]
        read_only_fields = ["email"]
