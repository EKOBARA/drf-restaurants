from django.db import models
from django.db.models.base import Model

# Create your models here.

# Restaurants Model 
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='images/', default='images/default.jpg')
    # owner: the user that created the resourse
    owner = models.ForeignKey(
        'users.User', related_name='restaurants', on_delete=models.CASCADE)

    def __str__(self):
       return self.name
    
# Review Model
class Review(models.Model):
    title = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant,
                                   on_delete=models.CASCADE,
                                   related_name='reviews'
                                   )
    body = models.TextField()
    # owner: the user that created the resource
    owner = models.ForeignKey(
        'users.User', related_name='reviews', on_delete=models.CASCADE,)
    # created: timestamp
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
