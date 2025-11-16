from geo.utils import hypotenuse, circle_area


def main() -> None:
    a = 3.0
    b = 4.0
    c = hypotenuse(a, b)
    area = circle_area(10.0)

    print(f"c = {c}")
    print(f"area = {area}")


if __name__ == "__main__":
    main()
