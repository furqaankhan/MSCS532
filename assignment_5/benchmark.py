"""Compare median sort times; input copies and checks are outside the timer."""

import platform
import random
import statistics
import time

from algorithms import deterministic_quicksort, randomized_quicksort


def main():
    print(f'Python {platform.python_version()}, {platform.system()} {platform.machine()}')
    print('Distribution  Size  Deterministic ms  Randomized ms')
    for distribution in ('random', 'sorted', 'reverse'):
        for size in (500, 1000, 2000, 4000):
            # Start with identical distinct keys for each distribution.
            data = list(range(size))
            if distribution == 'random':
                random.Random(100 + size).shuffle(data)
            elif distribution == 'reverse':
                data.reverse()
            # Compute the reference result once, outside the timed runs.
            expected = sorted(data)
            timings = []
            for sort in (deterministic_quicksort, randomized_quicksort):
                runs = []
                for repeat in range(5):
                    # Give each run a fresh copy and reproducible pivot sequence.
                    values = data.copy()
                    rng = random.Random(1000 + repeat)
                    start = time.perf_counter()
                    if sort is randomized_quicksort:
                        sort(values, rng)
                    else:
                        sort(values)
                    runs.append((time.perf_counter() - start) * 1000)
                    # Verify correctness only after stopping the timer.
                    assert values == expected
                # The median reduces the effect of an unusually slow run.
                timings.append(statistics.median(runs))
            print(f'{distribution:12} {size:5} {timings[0]:17.3f} {timings[1]:14.3f}')


if __name__ == '__main__':
    main()
