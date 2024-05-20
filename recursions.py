import random  # type:ignore
from typing import Any, Optional  # type:ignore
import math


def fac(n: int) -> float | int:
    if n == 1:
        return 1
    return n * fac(n - 1)


def draw_ruler(length: int, center_length: int):
    def draw_pattern(n: int):
        if n == 1:
            print('-')
            return

        draw_pattern(n - 1)
        print('-' * n)
        draw_pattern(n - 1)

    for i in range(length+1):
        print('-' * center_length, i)
        draw_pattern(center_length - 1)


# type: ignore
def binary_search(array: list[int], element: int) -> int:
    def search(array: list[int], element: int,  low: int, high: int) -> int:
        mid = (high + low // 2)
        if high < low:
            return -1
        if array[mid] == element:
            return mid
        if array[mid] < element:
            return search(array, element, low + 1, high)

        return search(array, element, low, high - 1)
    return search(array, element, 0, len(array) - 1)


def reverse(arr: list[Any], start: int, stop: int):
    if start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        reverse(arr, start + 1, stop - 1)


def pow(x: int | float, base: int | float) -> float | int:
    if base == 0:
        return 1
    return x * pow(x, base - 1)


def fast_power(x: int | float, base: int | float) -> float:
    if base == 0:
        return 1
    partial = fast_power(x, base // 2)
    result = partial * partial
    if base % 2 == 0:
        return result
    return result * x


def permuatations(phrase: list[str], store: list[str]):
    print(store, phrase)

    for index, letter in enumerate(phrase):
        store.append(letter)
        phrase.remove(letter)
        # print(store, phrase)
        print(''.join(store) + ''.join(phrase))
        permuatations(phrase, store)
        store.pop()
        phrase.insert(index, letter)


def maximum(arr: list, n=0, max=-math.inf):
    if n >= len(arr):
        return max
    return maximum(arr, n + 1, max if max > arr[n] else arr[n])


def n_harmonic(n):
    if n == 1:
        return 1
    return (1 / n) + n_harmonic(n - 1)


def integer(number: str):
    def inner(number, n=len(number)):
        if n == 0:
            return 0
        return (int(number[len(number) - n]) * 10**(n - 1)) + inner(number, n - 1)
    return inner(number)
