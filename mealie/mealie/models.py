from django.db import models

class Mealie(models.Model):
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrate = models.IntegerField()
    nutritionSet = models.CharField(max_length=200)

    def __str__(self):
        return f"P: {self.protein} F: {self.fat} K: {self.carbohydrate} Set: {self.nutritionSet}"