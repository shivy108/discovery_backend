from django.urls import path

from users.views import ListUsers, RetrieveUser, ListUpdateMeView

urlpatterns = [
    
    path('<int:user_id>/', RetrieveUser.as_view(), name='retrieve-user'),
    path('', ListUpdateMeView.as_view(), name='list-users'),
    path('', ListUsers.as_view()),
]
