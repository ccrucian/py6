from .elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strenght_potion() -> str:
    return (
            "Strenght potion brewed with "
            f"'{create_fire()}' and '{create_water()}'"
        )
