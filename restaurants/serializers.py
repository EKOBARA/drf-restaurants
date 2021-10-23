from rest_framework import serializers
from .models import Restaurant, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    restaurant = serializers.HyperlinkedRelatedField(
        view_name='restaurant_detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source='restaurant')

    class Meta:
        model = Review
        fields = ('restaurant', 'restaurant_id', 'title', 'body', 'owner')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # reviews = serializers.HyperlinkedRelatedField(
    #     view_name='review_detail',
    #     many=True,
    #     read_only=True
    # )

    # if you want to embed reviews in restaurant json response
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    restaurant_url = serializers.ModelSerializer.serializer_url_field(
        view_name='restaurant_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'cuisine', 'reviews',
                  'restaurant_url', 'owner', 'photo')
