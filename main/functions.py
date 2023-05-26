from typing import Tuple


def add(num1: Tuple[float, float], num2: Tuple[float, float]):
    return (num1[0] + num2[0], num1[1] + num2[1])


def multiply(num1: Tuple[float, float], num2: Tuple[float, float]):
    return ((num1[0] * num2[0]) - (num1[1] * num2[1]), (num1[0] * num2[1]) + (num1[1] * num2[0]))


def conjugate(num: Tuple[float, float]):
    return (num[0], -1 * num[0])
