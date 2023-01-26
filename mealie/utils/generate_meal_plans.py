import random
from .meal_plan import MealPlan, meal_plans
from .food_sets import nutrition_sets

def generate_meal_plans(set_name, goals):
    counter = 0
    while counter < 100000000:

        protein_goal = goals[0]
        fat_goal = goals[1]
        carbohydrate_goal = goals[2]
        nutrition_set = nutrition_sets[set_name]


        protein = protein_goal
        fat = fat_goal
        carbohydrate = carbohydrate_goal

        plan_array = []
        amounts_dictionary = {}

        for current_food in nutrition_set:
            if protein >= -10 and fat >= -5 and carbohydrate >= -10:
                current_food = random.choice(nutrition_set)
                if current_food not in plan_array:
                    random_recommended_amount = random.choice(current_food.recommended_amounts)
                    amounts_dictionary[current_food.name] = random_recommended_amount
                    protein -= current_food.protein * amounts_dictionary[current_food.name]
                    fat -= current_food.fat * amounts_dictionary[current_food.name]
                    carbohydrate -= current_food.carbs * amounts_dictionary[current_food.name]
                    plan_array.append(current_food)
                    counter += 1
        if -10 <= protein <= 10 and -5 <= fat <= 5 and -10 <= carbohydrate <= 10:
            meal_plan = MealPlan(plan_array, goals[0], goals[1], goals[2], amounts_dictionary)
            return meal_plan
