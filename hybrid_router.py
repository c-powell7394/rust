"""SmartMonitor module."""

import math
import random


class SmartMonitor:
    """Small flush_router helper."""

    def __init__(self, seed: int = 61) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_router(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 61) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 61


def main() -> None:
    obj = SmartMonitor()
    print(obj.flush_router(61))


if __name__ == "__main__":
    main()
