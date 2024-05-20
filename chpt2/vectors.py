from typing import Self, Iterable, Literal
import random


class Vector:

    def __init__(self, initial_values: Iterable[int | float] | int = []):
        if isinstance(initial_values, int):
            initial_values = (0 for _ in range(initial_values))

        self._values: list[float | int] = list(initial_values)
        self._k = -1

    def __len__(self) -> int:
        return len(self._values)

    def get_values(self) -> list[float | int]:
        return self._values

    def __getitem__(self, a: int) -> int | float:
        return self._values[a]

    def __next__(self) -> int | float:
        self._k += 1
        if self._k < len(self):
            return self._values[self._k]
        self._k = -1  # Reset the value of _k
        raise StopIteration

    def __iter__(self):
        return self

    def __add__(self, b: Self):
        if len(self) != len(b):
            raise ValueError('The two vectors should be of the same length')
        return Vector(list((b[i] + self[i] for i in range(len(self)))))

    def __neg__(self):
        return Vector((-1 * i for i in self))

    def __eq__(self, b: object) -> bool:
        if not isinstance(b, Vector):
            raise ValueError(
                f'Object {b} is not an instance of the Vector class')
        if not all(b) and not all(self):
            return True
        return self._values == b._values

    def __ne__(self, b: object) -> bool:
        return not (self == b)

    def __mul__(self, multiplier: float | int | Self):
        if isinstance(multiplier, float) or isinstance(multiplier, int):
            return Vector((i * multiplier for i in self))

        if isinstance(self, Vector) and len(self) == len(multiplier):
            return sum((self[i] * multiplier[i] for i in range(len(self))))

        raise ValueError(
            'Multiplier should either be a scalar or an instance of the Vector class with same length'
        )

    def __rmul__(self, scalar: float | int):
        return self * scalar

    def __sub__(self, b: Self):
        if len(self) != len(b):
            raise ValueError('The two vectors should be of the same length')
        return Vector((self[i] - b[i] for i in range(len(self))))

    def __str__(self) -> str:
        return f'<Vector[{len(self)}]: {self._values} >'


class Range:
    def __init__(self, start: int, stop: int | None = None, step: int | Literal[1] = 1):
        if stop is None:
            self._cur = 0
            self._stop = start
        else:
            self._cur = start
            self._stop = stop
        self._start = self._cur
        self._step = step
        self._cur -= step

    def __iter__(self):
        return self

    def __len__(self) -> int:
        return (self._stop + self._step - 1 - self._start) // self._step

    def __next__(self) -> int:
        self._cur += self._step
        if self._cur < self._stop:
            return self._cur
        raise StopIteration


vector1 = Vector((random.randint(1, 100) for _ in range(3)))
print(vector1, vector1 * vector1, Vector(10),
      (vector1 * 2) == (2 * vector1), sep='\n')
