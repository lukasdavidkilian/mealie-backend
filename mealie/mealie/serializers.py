from rest_framework import serializers
from .models import Mealie


class MealieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mealie
        fields = ['id', 'protein', 'fat', 'carbohydrate', 'nutritionSet']


# class MealPlanSerializer(serializers.ModelSerializer):
#   class Meta:
#      model = MealPlan
#     fields = ['food', 'protein_goal', 'fat_goal', 'carbohydrate_goal', 'dict']


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        food = serializers.ListField()
        protein_goal = serializers.IntegerField()
        fat_goal = serializers.IntegerField()
        carbohydrate_goal = serializers.IntegerField()
        dict = serializers.DictField()
