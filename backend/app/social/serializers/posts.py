from app.social.models.posts import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "user", "content", "created"]
        read_only_fields = ["user"]
