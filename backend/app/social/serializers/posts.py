from app.social.models.posts import Post
from rest_framework import serializers
from app.users.serializers import UserSerializer


class GetPostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
