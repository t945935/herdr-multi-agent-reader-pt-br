"""Chapter 1: um contrato deliberadamente pequeno para um exercício de desenvolvimento e revisão."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Era esperado um número, exceto bool")
    if not isfinite(value):
        raise ValueError("Era esperado um número finito")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return a / b
