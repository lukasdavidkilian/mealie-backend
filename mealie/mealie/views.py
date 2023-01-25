import json

from django.http import JsonResponse
from .models import Mealie
from .serializers import MealieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.generate_meal_plans import generate_meal_plans

@api_view(['GET', 'POST'])
def mealie_list(request):

    if request.method == 'GET':
        mealies = Mealie.objects.all()
        serializer = MealieSerializer(mealies, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = MealieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    data = request.data
    protein_goal = int(data.get('protein'))
    fat_goal = int(data.get('fat'))
    carb_goal = int(data.get('carbohydrate'))
    nutrition_set = data.get('nutritionSet')
    goals = [protein_goal, fat_goal, carb_goal]
        # Use the provided goals and nutrition set to generate the meal plan
    meal_plan = generate_meal_plans(nutrition_set, goals)

    return JsonResponse(meal_plan.__str__, status=status.HTTP_200_OK)


  #if request.method == 'POST':
       # serializer = MealieSerializer(data = request.data)
       # if serializer.is_valid():
           # serializer.save()
           # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #