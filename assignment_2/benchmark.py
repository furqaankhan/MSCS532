"""Compare sorting time and extra Python memory using the standard library."""
import gc
import random
from statistics import median
from time import perf_counter_ns
import tracemalloc

from algorithms import merge_sort, quick_sort


def compare(sizes=(250, 500, 1000, 2000, 4000), repeats=5):
    algorithms = (merge_sort, quick_sort)
    print(f"{'Size':>5} {'Data':<8} {'Algorithm':<12} {'Time (ms)':>10} {'Peak (KiB)':>11}")

    for size in sizes:
        for kind in ('sorted', 'reverse', 'random'):
            times = {sort: [] for sort in algorithms}
            memory = {sort: [] for sort in algorithms}

            # Warm up both algorithms before collecting measurements.
            for sort in algorithms:
                values = list(range(size))
                if kind == 'reverse':
                    values.reverse()
                elif kind == 'random':
                    random.Random(532).shuffle(values)
                sort(values)

            for trial in range(repeats):
                original = list(range(size))
                if kind == 'reverse':
                    original.reverse()
                elif kind == 'random':
                    random.Random(532 + trial).shuffle(original)
                expected = sorted(original)

                # Alternate order; both algorithms receive the same input.
                order = algorithms if trial % 2 == 0 else algorithms[::-1]
                for sort in order:
                    values = original.copy()
                    gc.collect()
                    start = perf_counter_ns()
                    sort(values)
                    times[sort].append((perf_counter_ns() - start) / 1_000_000)
                    assert values == expected

                    # Measure memory separately so tracing does not affect timing.
                    values = original.copy()
                    gc.collect()
                    tracemalloc.start()
                    try:
                        sort(values)
                        _, peak = tracemalloc.get_traced_memory()
                    finally:
                        tracemalloc.stop()
                    memory[sort].append(peak / 1024)
                    assert values == expected

            for sort in algorithms:
                print(f'{size:5} {kind:<8} {sort.__name__:<12} '
                      f'{median(times[sort]):10.3f} {median(memory[sort]):11.3f}',
                      flush=True)


if __name__ == '__main__':
    compare()
