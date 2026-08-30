"""CoreClient module."""

import math
import random


class CoreClient:
    """Small encode_monitor helper."""

    def __init__(self, seed: int = 96) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_monitor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 96) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 96


def main() -> None:
    obj = CoreClient()
    print(obj.encode_monitor(96))


if __name__ == "__main__":
    main()
