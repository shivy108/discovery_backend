from rest_framework import serializers
from social.models.friends import Friend
from users.serializers import UserSerializer


class FriendSerializer(serializers.ModelSerializer):
    requester = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Friend
        fields = ['id', 'requester', 'receiver', 'status', 'created']
