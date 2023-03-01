def divisionEntera(dividendo: int, divisor: int) -> int:
    """
    POST: Devuelve el resultado de la division entera entre el dividendo y el divisor ingresados.
    TESTS:
    >>> divisionEntera(10, 3)
    3
    >>> divisionEntera(15, 1)
    15
    >>> divisionEntera(12, 0)
    Traceback (most recent call last):
    ...
    ValueError: No se puede dividir por cero.
    """
    if divisor == 0:
        raise ValueError("No se puede dividir por cero.")
    return dividendo // divisor
