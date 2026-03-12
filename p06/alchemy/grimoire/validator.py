def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    ingredients_lower = ingredients.lower()

    for element in valid_elements:
        if element in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
