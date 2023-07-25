from django.db import models
from django.contrib.auth.models import User



class Food(models.Model):
    
    FOOD_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snack', 'Snack'),
        ('Dinner', 'Dinner')
    )
    
    food_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    description = models.TextField()
    feed = models.IntegerField(default=0)
    food_type = models.CharField(max_length=30, choices=FOOD_CHOICES)
    cooked_time = models.DateTimeField()
    #image = models.ImageField()
    address = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.food_name