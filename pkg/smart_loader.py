"""AtomicAdapter module."""

import math
import random


class AtomicAdapter:
    """Small render_monitor helper."""

    def __init__(self, seed: int = 74) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_monitor(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 74) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 74


def main() -> None:
    obj = AtomicAdapter()
    print(obj.render_monitor(74))


if __name__ == "__main__":
    main()
