import alchemy
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmutinf Lead to Gold: "
        f"brew '{alchemy.create_air()}' and"
        f" '{alchemy.strenght_potion()}' mixed with"
        f" {create_fire()}"
    )