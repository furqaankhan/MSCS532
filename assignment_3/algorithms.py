"""Quicksort variants and a chained hash table for integer keys."""

import random


def _quicksort(values, randomized):
    # An explicit stack avoids Python's recursion limit on unbalanced inputs.
    pending = [(0, len(values) - 1)]
    while pending:
        low, high = pending.pop()
        if low >= high:
            continue
        pivot_index = random.randint(low, high) if randomized else low
        pivot = values[pivot_index]
        values[low], values[pivot_index] = values[pivot_index], values[low]
        # Three-way partition keeps duplicate values out of both subproblems.
        lt, i, gt = low, low + 1, high
        while i <= gt:
            if values[i] < pivot:
                values[lt], values[i] = values[i], values[lt]
                lt += 1
                i += 1
            elif values[i] > pivot:
                values[i], values[gt] = values[gt], values[i]
                gt -= 1
            else:
                i += 1
        pending.append((low, lt - 1))
        pending.append((gt + 1, high))
    return values


def randomized_quicksort(values):
    return _quicksort(values, True)


def deterministic_quicksort(values):
    return _quicksort(values, False)


class HashTable:
    """Integer keys in [0, 2**61 - 1); missing keys raise KeyError."""

    PRIME = 2**61 - 1

    def __init__(self, seed=None):
        rng = random.Random(seed)
        self.a = rng.randrange(1, self.PRIME)
        self.b = rng.randrange(self.PRIME)
        self.buckets = [[] for _ in range(8)]
        self.size = 0

    def _index(self, key):
        if not isinstance(key, int) or not 0 <= key < self.PRIME:
            raise ValueError('key must be an integer in [0, 2**61 - 1)')
        return ((self.a * key + self.b) % self.PRIME) % len(self.buckets)

    def insert(self, key, value):
        bucket = self.buckets[self._index(key)]
        for index, (existing, _) in enumerate(bucket):
            if existing == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size > len(self.buckets):
            old = self.buckets
            self.buckets = [[] for _ in range(2 * len(old))]
            for chain in old:
                for old_key, old_value in chain:
                    self.buckets[self._index(old_key)].append((old_key, old_value))

    def search(self, key):
        for existing, value in self.buckets[self._index(key)]:
            if existing == key:
                return value
        raise KeyError(key)

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for index, (existing, _) in enumerate(bucket):
            if existing == key:
                del bucket[index]
                self.size -= 1
                return
        raise KeyError(key)
