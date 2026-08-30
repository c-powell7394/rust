"""SecureDispatcher module."""

import math
import random


class SecureDispatcher:
    """Small run_monitor helper."""

    def __init__(self, seed: int = 69) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_monitor(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 69) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 69


def main() -> None:
    obj = SecureDispatcher()
    print(obj.run_monitor(69))


if __name__ == "__main__":
    main()
