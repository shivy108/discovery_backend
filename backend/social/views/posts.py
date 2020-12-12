from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

from social.models.posts import Post
from social.serializers.posts import GetPostSerializer, PostSerializer


class ListCreatePosts(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created')

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetPostSerializer
        return PostSerializer
