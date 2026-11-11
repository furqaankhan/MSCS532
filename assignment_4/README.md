# Assignment 4: Heap Data Structures

This assignment implements in-place Heapsort, compares it with randomized Quicksort and Merge Sort, and uses an indexed max-heap for nonpreemptive priority scheduling. The report explains the algorithms, results, and limitations.

Python 3.9 or newer is required; no external packages are needed. From the repository root:

```bash
python3 assignment_4/benchmark.py
python3 assignment_4/scheduler.py
python3 -m unittest discover -s assignment_4 -p 'test*.py'
```

The benchmark times five runs on each seeded input and reports medians; copying and correctness checks are outside the timed interval. On the recorded machine, Merge Sort was fastest in the tested cases, though timings vary. Heapsort modifies and returns its input list. The queue uses higher numbers for higher priority and insertion order to break ties; `change_priority` supports both increases and decreases by task ID. The simulation runs each selected task to completion, so a higher-priority arrival cannot interrupt it and a deadline can be missed.
