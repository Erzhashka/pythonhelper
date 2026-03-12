def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import to avoid circular dependency
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if "INVALID" not in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
