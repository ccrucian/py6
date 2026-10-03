import alchemy


def main() -> None:
    print(f"{alchemy.create_air()}")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError as e:
        print(
            f"Function not exposed through the module "
            f"interface: {e}")


if __name__ == "__main__":
    main()
