"""Compare sorts on identical seeded inputs, reporting median milliseconds."""
import platform
import random
import statistics
import time
from algorithms import heapsort, quicksort, merge_sort


def main():
    rng = random.Random(532)
    print('Python', platform.python_version(), '|', platform.platform())
    print('Seed 532; five runs; median milliseconds; input copies excluded')
    print('distribution,size,heap,quick,merge')
    for kind in ('random', 'sorted', 'reverse'):
        for n in (500, 1000, 2000, 4000):
            source = list(range(n))
            if kind == 'random': rng.shuffle(source)
            elif kind == 'reverse': source.reverse()
            expected = sorted(source)
            medians = []
            for sort in (heapsort, quicksort, merge_sort):
                times = []
                for run in range(5):
                    values = source.copy()
                    random.seed(532 + run)
                    start = time.perf_counter()
                    sort(values)
                    times.append((time.perf_counter() - start) * 1000)
                    assert values == expected
                medians.append(statistics.median(times))
            print(f'{kind},{n},' + ','.join(f'{m:.3f}' for m in medians))


if __name__ == '__main__': main()
