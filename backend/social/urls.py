from django.urls import path, include
from social.views.posts import ListCreatePosts
from social.views.comments import ListCreateComment
from social.views.friends import CreateFriendRequest, RetrieveUpdateDestroyFriendRequest, ListFriendRequests, ListFriends

post_patterns = [
    path('', ListCreatePosts.as_view(), name='list-create-posts')
]

comment_patterns = [
    path("<int:post_id>/", ListCreateComment.as_view(),
         name="list-create-post-comment"),
]

friend_patterns = [
    path('request/<int:user_id>/', CreateFriendRequest.as_view(),
         name='create-friend-request'),
    path('requests/<int:friend_request_id>/', RetrieveUpdateDestroyFriendRequest.as_view(),
         name='retrieve-update-destroy-friend-request'),
    path('requests/', ListFriendRequests.as_view(), name='list-friend-request'),
    path('', ListFriends.as_view(), name='list-friends'),
]


urlpatterns = [
    path('posts/', include(post_patterns)),
    path('comments/', include(comment_patterns)),
    # path('followers/', include(follow_patterns)),
    path('friends/', include(friend_patterns)),
]
