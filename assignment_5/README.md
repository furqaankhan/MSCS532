# Assignment 5: Quicksort

This assignment implements in-place deterministic and randomized Quicksort and compares their running times. Both use the same two-way partition; the deterministic version picks the last element, while the randomized version picks a uniformly random element from the active subarray. Both return the input list. Recursing on the smaller side limits stack space, even for unbalanced partitions.

Python 3.9 or newer is required; no external packages are needed. From the repository root:

```bash
python3 assignment_5/benchmark.py
python3 -m unittest discover -s assignment_5 -p 'test*.py'
```

The benchmark uses seeded inputs and pivot choices, reporting the median of five timings. Copies and correctness checks are outside the timed interval. On the recorded machine, the deterministic version was faster on random permutations but much slower on sorted and reverse-sorted inputs. Timings vary by machine and run. Both implementations take quadratic time on all-equal input because this partition groups equal values on one side. See the report for analysis and results.
