from rest_framework import generics, serializers  # <- import generics
from .models import Restaurant, Review  # <- don't forget your models
from .serializers import RestaurantSerializer, ReviewSerializer 
from rest_framework import permissions
from restaurants.permissions import IsOwnerOrReadOnly

# Create your views here.


class RestaurantList(generics.ListCreateAPIView):
    # add code here
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # default permissions (anon is read only, authenticated can create)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    # add code here
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # only owner can create and destroy
    permission_classes = [IsOwnerOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    # add code here
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # default permissions (anon is read only, authenticated can create)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # add code here
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # only owner can create and destroy
    permission_classes = [IsOwnerOrReadOnly]
