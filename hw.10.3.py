from inspect import isgenerator
from typing import Callable, Generator


def pow(x: int) -> int:
    """Повертає квадрат числа."""
    return x ** 2


def some_gen(begin: int, n: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    """Генератор n значень, починаючи з begin, використовуючи функцію func."""
    value = begin
    for _ in range(n):
        yield value
        value = func(value)


gen = some_gen(2, 4, pow)

assert isgenerator(gen) is True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'

print('OK')
