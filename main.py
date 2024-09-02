# Dein Code kommt hier hin
"""
mod doc
"""
import json


def load_recipe(recipies: str) -> dict:
    loaded_recipies = json.loads(recipies)
    return loaded_recipies

def adjust_recipe(recepie: dict, people:int) -> dict:
    adjusted_ingredients = {}
    original_servings = recepie["servings"]
    factor = people / original_servings

    for ingredient, amount in recepie["ingredients"].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjusted_recipe = {
        "title": recepie["title"],
        "ingredients": adjusted_ingredients,
        "servings": people
    }
    return adjusted_recipe










if __name__ == "__main__":
    pass


