from rest_framework.generics import ListCreateAPIView
from app.social.models.posts import Post
from app.social.serializers.posts import PostSerializer, GetPostSerializer



class ListCreatePosts(ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetPostSerializer
        return PostSerializer
