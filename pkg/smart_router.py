"""LocalBuilder module."""

import math
import random


class LocalBuilder:
    """Small sync_session helper."""

    def __init__(self, seed: int = 44) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_session(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 44) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 44


def main() -> None:
    obj = LocalBuilder()
    print(obj.sync_session(44))


if __name__ == "__main__":
    main()
