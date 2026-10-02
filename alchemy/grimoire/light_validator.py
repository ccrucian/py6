from  .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    text = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    valid = False
    for item in allowed:
        if item in text:
            valid = True
            break
    if valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"