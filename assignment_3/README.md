# Assignment 3: Algorithm Efficiency and Scalability

This assignment compares randomized and first-pivot Quicksort and implements a hash table with chaining. The report contains the analysis and measured results.

Python 3.9 or newer is required; no external packages are needed. From the repository root, run:

```bash
python3 assignment_3/benchmark.py
```

The script uses seeded input, five runs per case, and reports median times. Both sorts modify and return the input list. The hash table accepts integer keys from 0 through 2**61 - 2. `insert(key, value)` adds or updates a key; `search(key)` returns its value; `delete(key)` removes it. Searching for or deleting an absent key raises `KeyError`.

In the recorded run, randomized Quicksort was much faster on reverse-sorted input; the first-pivot version was generally faster on random input. Three-way partitioning made both efficient on the repeated-value inputs. Actual timings vary by machine and run.
