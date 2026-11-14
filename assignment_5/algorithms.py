"""In-place Quicksort with deterministic or uniformly random pivots."""

import random


def _quicksort(values, low, high, rng):
    # The active interval includes both low and high. A zero- or one-item
    # interval is already sorted, so it needs no partition.
    while low < high:
        # Select the last item or draw a pivot uniformly from this interval.
        pivot_index = high if rng is None else rng.randrange(low, high + 1)
        values[pivot_index], values[high] = values[high], values[pivot_index]
        pivot = values[high]
        # Items before boundary are at most the pivot; items from boundary
        # to index are greater. The pivot stays at high during the scan.
        boundary = low
        for index in range(low, high):
            if values[index] <= pivot:
                values[boundary], values[index] = values[index], values[boundary]
                boundary += 1
        # Put the pivot between the two groups, in its final sorted position.
        values[boundary], values[high] = values[high], values[boundary]
        # Sort the smaller side recursively, then continue with the larger
        # side in this frame. This keeps the call stack logarithmic.
        if boundary - low < high - boundary:
            _quicksort(values, low, boundary - 1, rng)
            low = boundary + 1
        else:
            _quicksort(values, boundary + 1, high, rng)
            high = boundary - 1


def deterministic_quicksort(values):
    """Sort and return the same list, choosing the last element as pivot."""
    # None selects the fixed last-element pivot.
    _quicksort(values, 0, len(values) - 1, None)
    return values


def randomized_quicksort(values, rng=None):
    """Sort and return the same list, choosing a random pivot per partition."""
    # An optional generator lets the benchmark reproduce pivot choices.
    _quicksort(values, 0, len(values) - 1, rng if rng is not None else random)
    return values
