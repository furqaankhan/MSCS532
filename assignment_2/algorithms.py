"""Two ascending, in-place sorting interfaces; no built-in sorting is used."""


def merge_sort(values):
    """Stable top-down Merge Sort: Θ(n log n) time, Θ(n) auxiliary space."""
    auxiliary = [None] * len(values)

    def sort(lo, hi):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid, hi)
        # Copy this range into a reusable buffer, avoiding recursive slices.
        for k in range(lo, hi):
            auxiliary[k] = values[k]
        left, right = lo, mid
        for k in range(lo, hi):
            # Take the left equal item first to preserve stability.
            if left < mid and (right >= hi or auxiliary[left] <= auxiliary[right]):
                values[k] = auxiliary[left]
                left += 1
            else:
                values[k] = auxiliary[right]
                right += 1

    sort(0, len(values))


def quick_sort(values):
    """Lomuto Quick Sort with last pivot and O(log n) maximum call depth.

    Recurse only into the smaller partition; iterate over the larger one.
    This controls stack space but does not prevent quadratic running time.
    """
    def partition(lo, hi):
        pivot = values[hi]
        boundary = lo
        for scan in range(lo, hi):
            if values[scan] <= pivot:
                values[boundary], values[scan] = values[scan], values[boundary]
                boundary += 1
        values[boundary], values[hi] = values[hi], values[boundary]
        return boundary

    def sort(lo, hi):
        while lo < hi:
            pivot_index = partition(lo, hi)
            # Every recursive subproblem has at most half as many items.
            if pivot_index - lo < hi - pivot_index:
                sort(lo, pivot_index - 1)
                lo = pivot_index + 1
            else:
                sort(pivot_index + 1, hi)
                hi = pivot_index - 1

    sort(0, len(values) - 1)


if __name__ == '__main__':
    sample = [5, -2, 9, 1, 5, 0]
    for algorithm in (merge_sort, quick_sort):
        data = sample.copy()
        algorithm(data)
        print(f'{algorithm.__name__}: {sample} -> {data}')
