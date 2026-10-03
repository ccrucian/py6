from ..elements import create_air
from ..potions import strenght_potion
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and"
        f" '{strenght_potion()}' mixed with"
        f" {create_fire()}"
    )
