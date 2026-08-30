"""HybridMonitor module."""

import math
import random


class HybridMonitor:
    """Small collect_resolver helper."""

    def __init__(self, seed: int = 51) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_resolver(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 51) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 51


def main() -> None:
    obj = HybridMonitor()
    print(obj.collect_resolver(51))


if __name__ == "__main__":
    main()
