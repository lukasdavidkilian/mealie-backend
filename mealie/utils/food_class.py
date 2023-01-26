import json

class Food:
    def __init__(self, name, protein, fat, carbs, amount, unit, recommended_amounts):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.amount = amount
        self.unit = unit
        self.recommended_amounts = recommended_amounts

    def to_json(self):

        json_dict = {
            'name': self.name,
            'protein': self.protein,
            'fat': self.fat,
            'carbs': self.carbs,
            'amount': self.amount,
            'unit': self.unit,
            'recommended_amounts': self.recommended_amounts
        }

        return json.dumps(json_dict)

