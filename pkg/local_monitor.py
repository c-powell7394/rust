"""HybridDispatcher module."""

import math
import random


class HybridDispatcher:
    """Small fetch_engine helper."""

    def __init__(self, seed: int = 72) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_engine(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 72) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 72


def main() -> None:
    obj = HybridDispatcher()
    print(obj.fetch_engine(72))


if __name__ == "__main__":
    main()
