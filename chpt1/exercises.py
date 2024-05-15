from typing import Iterable, Any
import math
import random

#  Exercise R-1.1
def is_multiple(m: int, n: int) -> bool: 
    return n % m == 0

# Exercise R-1.2
def is_even(n: int) -> bool: 
    return n % 2 == 0

# Exercise R-1.3
def minmax(n: Iterable[int|float]) -> tuple[int | float, int| float]: 
    min = math.inf
    max =  -math.inf
    for x in n: 
        if min > x: 
            min = x 
        if max < x: 
            max = x
    return min, max


# Exercise R-1.4
def sum_square_smaller_than_n(n: int) -> int : 
    return sum((x**2 for x in range(1,n)))


# Exercise R-1.5: See R-1.4


# Exercise R-1.6
def sum_square_odd_smaller_than_n(n: int) -> int : 
    return sum((x**2 for x in range(1, n) if x % 2 != 0))



# Exercise R-1.7: see R-1.6

# C-1.13
def reverse(n: list[Any]): 
    length = len(n)
    for x in range(length //2):
        n[x], n[length - x - 1] = n[length -x -1], n[x]

# C-1.14
def distinct_pair(n: list[Any]) -> bool: 
    return True

# C-1.18
def shuffle(elements: list[Any]):
    length = len(elements) 
    for x in range(length):
        pos = random.randint(0, length - 1) 
        elements[x], elements[pos] = elements[pos], elements[x]

# C-1.21
def print_reverse_on_EOR_Error(): 
    store: list[Any] = []
    try: 
        while True: 
            store.append(input("Type Something: "))
    except EOFError: 
        for x in range(len(store) -1, -1, -1): 
            print(store[x])
        raise

# C-1.27
def factors(n: int|float) -> list[int|float]: 
    output: list[int|float] = []
    i = 1
    while i * i < n: 
        if n % i == 0: 
            output.append(i)
            output.append(n / i)
        i += 1
    if i * i == n: 
        output.append(i)
    return sorted(output)


# C-1.28
def p_norm(v: list[int|float], p: int) -> float: 
    total = sum((x ** p for x in v))
    return total ** .25

print(p_norm([1,2,3,23,43], 24))