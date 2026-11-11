"""Three ascending sorts used in the timing comparison."""
import random


def heapsort(values):
    """Sort the list in place using a max-heap and return it."""
    def sift(root, end):
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and values[child] < values[child + 1]:
                child += 1
            if values[root] >= values[child]:
                break
            values[root], values[child] = values[child], values[root]
            root = child

    n = len(values)
    for root in range(n // 2 - 1, -1, -1):
        sift(root, n)
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        sift(0, end)
    return values


def quicksort(values):
    """Random-pivot, three-way Quicksort with an explicit stack."""
    stack = [(0, len(values) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        pivot = values[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if values[i] < pivot:
                values[lt], values[i] = values[i], values[lt]
                lt += 1; i += 1
            elif values[i] > pivot:
                values[i], values[gt] = values[gt], values[i]
                gt -= 1
            else:
                i += 1
        stack.extend(((lo, lt - 1), (gt + 1, hi)))
    return values


def merge_sort(values):
    """Bottom-up Merge Sort using an auxiliary list."""
    n = len(values)
    source, target = values, values.copy()
    width = 1
    while width < n:
        for start in range(0, n, 2 * width):
            middle, end = min(start + width, n), min(start + 2 * width, n)
            i, j = start, middle
            for k in range(start, end):
                if j >= end or (i < middle and source[i] <= source[j]):
                    target[k] = source[i]; i += 1
                else:
                    target[k] = source[j]; j += 1
        source, target = target, source
        width *= 2
    if source is not values:
        values[:] = source
    return values
