"""SimpleDispatcher module."""

import math
import random


class SimpleDispatcher:
    """Small flush_client helper."""

    def __init__(self, seed: int = 94) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_client(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 94) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 94


def main() -> None:
    obj = SimpleDispatcher()
    print(obj.flush_client(94))


if __name__ == "__main__":
    main()
