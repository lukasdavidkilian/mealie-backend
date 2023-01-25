from rest_framework import serializers
from .models import Mealie

class MealieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mealie
        fields = ['id', 'protein', 'fat', 'carbohydrate', 'nutritionSet']

#class MealPlanSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = MealPlan
   #     fields = ['food', 'protein_goal', 'fat_goal', 'carbohydrate_goal', 'dict']