"""DynamicController module."""

import math
import random


class DynamicController:
    """Small encode_client helper."""

    def __init__(self, seed: int = 20) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_client(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 20) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 20


def main() -> None:
    obj = DynamicController()
    print(obj.encode_client(20))


if __name__ == "__main__":
    main()
