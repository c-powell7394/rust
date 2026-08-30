"""SecureResolver module."""

import math
import random


class SecureResolver:
    """Small encode_processor helper."""

    def __init__(self, seed: int = 23) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_processor(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 23) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 23


def main() -> None:
    obj = SecureResolver()
    print(obj.encode_processor(23))


if __name__ == "__main__":
    main()
