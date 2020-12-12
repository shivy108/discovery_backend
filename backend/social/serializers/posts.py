from rest_framework import serializers

from social.models.posts import Post
from users.serializers import UserSerializer


class GetPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
