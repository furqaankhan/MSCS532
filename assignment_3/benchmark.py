"""Compare both sorts using identical inputs; report median milliseconds."""
import platform
import random
import statistics
import time
from algorithms import deterministic_quicksort, randomized_quicksort


def main():
    rng = random.Random(532)
    print('Python', platform.python_version(), '|', platform.platform())
    print('Seed: 532; 5 runs; median milliseconds; input copying excluded')
    print('distribution,size,randomized_ms,deterministic_ms')
    for kind in ('random', 'sorted', 'reverse', 'repeated'):
        for n in (500, 1000, 2000, 4000):
            if kind == 'random':
                source = list(range(n)); rng.shuffle(source)
            elif kind == 'sorted':
                source = list(range(n))
            elif kind == 'reverse':
                source = list(range(n, 0, -1))
            else:
                source = [rng.randrange(10) for _ in range(n)]
            expected = sorted(source)
            medians = []
            for func in (randomized_quicksort, deterministic_quicksort):
                timings = []
                for run in range(5):
                    values = source.copy()
                    random.seed(532 + run)
                    start = time.perf_counter()
                    func(values)
                    timings.append((time.perf_counter() - start) * 1000)
                    assert values == expected
                medians.append(statistics.median(timings))
            print(f'{kind},{n},{medians[0]:.3f},{medians[1]:.3f}')


if __name__ == '__main__':
    main()
