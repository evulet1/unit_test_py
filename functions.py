from typing import Union


def divide(divident: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")
    return divident / divisor

def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("At least one value to multiply must be passed.")

    total = 1
    for arg in args:
        total *= arg

    return total