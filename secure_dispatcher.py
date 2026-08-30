"""SimpleEngine module."""

import math
import random


class SimpleEngine:
    """Small sync_monitor helper."""

    def __init__(self, seed: int = 66) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_monitor(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 66) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 66


def main() -> None:
    obj = SimpleEngine()
    print(obj.sync_monitor(66))


if __name__ == "__main__":
    main()
