from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    amount_of_reviews = serializers.SerializerMethodField(read_only=True)

    def get_amount_of_reviews(self, restaurant):
        return restaurant.reviews.count()

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'location',
                  'first_name',
                  'last_name',
                  'profile_picture',
                  'profile_description',
                  'amount_of_reviews'
                  ]
        read_only_fields = ['email']
