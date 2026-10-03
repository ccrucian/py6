def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(
        spell_name: str, ingredients: str
        ) -> str:
    from .light_validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"Not recorded: {spell_name} ({validation})"
    return f"Recorded: {spell_name} ({validation})"
