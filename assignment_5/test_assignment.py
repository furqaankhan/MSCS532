import random
import unittest

from algorithms import deterministic_quicksort, randomized_quicksort


class QuicksortTests(unittest.TestCase):
    def test_sorts_varied_inputs_in_place(self):
        rng = random.Random(42)
        cases = [[], [1], [2, 1], list(range(200)), list(range(200, 0, -1)),
                 [3] * 200, [rng.randrange(-10, 11) for _ in range(500)]]
        for sort in (deterministic_quicksort, randomized_quicksort):
            for case in cases:
                with self.subTest(sort=sort.__name__, size=len(case)):
                    values = case.copy()
                    result = sort(values)
                    self.assertIs(result, values)
                    self.assertEqual(values, sorted(case))

    def test_large_ordered_input_does_not_exhaust_recursion(self):
        for sort in (deterministic_quicksort, randomized_quicksort):
            values = list(range(1500))
            self.assertEqual(sort(values), list(range(1500)))


if __name__ == '__main__':
    unittest.main()
