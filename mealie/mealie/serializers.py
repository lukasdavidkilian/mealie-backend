from rest_framework import serializers
from .models import Mealie

class MealieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mealie
        fields = ['id', 'protein', 'fat', 'carbohydrate', 'nutritionSet']