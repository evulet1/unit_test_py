from typing import Union


def divide(divident: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")
    return divident / divisor
