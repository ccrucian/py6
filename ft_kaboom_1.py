from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    x  = dark_spell_record(
        "Fantasy", "Mat, frog, duck"
    )
    print(f"{x}")


if __name__ == "__main__":
    main()


