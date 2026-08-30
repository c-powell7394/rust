"""LiteFactory module."""

import math
import random


class LiteFactory:
    """Small collect_processor helper."""

    def __init__(self, seed: int = 49) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_processor(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 49) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 49


def main() -> None:
    obj = LiteFactory()
    print(obj.collect_processor(49))


if __name__ == "__main__":
    main()
