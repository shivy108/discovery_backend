from django.urls import path, include
from app.social.views.posts import ListCreatePosts


post_patterns = [
    path('', ListCreatePosts.as_view(), name='list-create-posts')
]

urlpatterns = [
    path('posts/', include(post_patterns))
    # path('comments/', include(comment_patterns)),
    # path('followers/', include(follow_patterns)),
    # path('friends/', include(friend_patterns)),
]
