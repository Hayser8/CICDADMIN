"""Operaciones matemáticas básicas para la práctica de integración continua."""

from numbers import Real


def _require_integer(value, name):
    """Valida un entero sin aceptar booleanos, aunque bool herede de int."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} debe ser un número entero")


def square(number):
    """Retorna el cuadrado de un número real."""
    if isinstance(number, bool) or not isinstance(number, Real):
        raise TypeError("number debe ser un número real")
    # CAMBIAR ESTA LINEAA.
    return number * number


def factorial(number):
    """Retorna el factorial de un entero no negativo; 0! es 1."""
    _require_integer(number, "number")
    if number < 0:
        raise ValueError("number debe ser un entero no negativo")

    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def is_prime(number):
    """Indica si un entero es primo; los enteros menores que 2 no lo son."""
    _require_integer(number, "number")
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def gcd(a, b):
    """Retorna el máximo común divisor no negativo de dos enteros."""
    _require_integer(a, "a")
    _require_integer(b, "b")

    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Retorna el mínimo común múltiplo no negativo de dos enteros."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
