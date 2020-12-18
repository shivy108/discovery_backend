from django.urls import path, include
from social.views.posts import ListCreatePosts
from social.views.comments import ListCreateComment


post_patterns = [
    path('', ListCreatePosts.as_view(), name='list-create-posts')
]

comment_patterns = [
    path("<int:post_id>/", ListCreateComment.as_view(),
         name="list-create-post-comment"),
]


urlpatterns = [
    path('posts/', include(post_patterns)),
    path('comments/', include(comment_patterns)),
    # path('followers/', include(follow_patterns)),
    # path('friends/', include(friend_patterns)),
]
