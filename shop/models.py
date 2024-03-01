from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name=models.CharField(max_length=30)
    meal_type=models.CharField(max_length=30)
    Ingredients=models.CharField(max_length=30)
    desc=models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    rating=models.FloatField()
    review=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.name
