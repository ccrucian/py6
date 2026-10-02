from alchemy import grimoire


def main() -> None:
    x  = grimoire.light_spell_record(
        "Fantasy", "Mat, frog, duck"
    )
    print(f"{x}")


if __name__ == "__main__":
    main()


