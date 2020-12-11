from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated


from app.users.serializers import UserSerializer
from rest_framework.response import Response

User = get_user_model()


class ListUsers(ListAPIView):
    """
    List all Users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    search_fields = ["username"]
    filter_backends = (filters.SearchFilter,)


class RetrieveUser(RetrieveAPIView):
    """
    Retrieve a user by ID
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"


class ListUpdateMeView(GenericAPIView):
    """
    List / Update current User.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        queryset = User.objects.get(username=self.request.user)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        queryset = User.objects.get(username=self.request.user)
        serializer = self.get_serializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
