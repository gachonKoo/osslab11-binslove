import math


def hypotenuse(a: float, b: float) -> float:
    """직각삼각형에서 두 변 a, b가 주어졌을 때 빗변 c를 반환한다."""
    return (a ** 2 + b ** 2) ** 0.5


def circle_area(radius: float) -> float:
    """반지름 radius인 원의 넓이를 반환한다."""
    return math.pi * radius ** 2
