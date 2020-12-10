from rest_framework.generics import (
    ListCreateAPIView
)
from app.social.models.posts import Post
from app.social.serializers.posts import PostSerializer


class ListCreatePosts(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all().order_by("-created")
        return self.filter_posts(posts)
