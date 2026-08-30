"""LocalRouter module."""

import math
import random


class LocalRouter:
    """Small dispatch_adapter helper."""

    def __init__(self, seed: int = 34) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_adapter(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 34) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 34


def main() -> None:
    obj = LocalRouter()
    print(obj.dispatch_adapter(34))


if __name__ == "__main__":
    main()
