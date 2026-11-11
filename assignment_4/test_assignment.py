import random
import unittest
from algorithms import heapsort, quicksort, merge_sort
from scheduler import Task, PriorityQueue, simulate


class AssignmentTests(unittest.TestCase):
    def test_sorts(self):
        rng = random.Random(532)
        for values in ([], [1], [3, 2, 1], [4] * 20, [rng.randrange(10) for _ in range(200)]):
            for sort in (heapsort, quicksort, merge_sort):
                data = values.copy()
                self.assertEqual(sort(data), sorted(values))

    def test_queue_updates_and_ties(self):
        q = PriorityQueue()
        for task in (Task('a', 1, 0, 4, 2), Task('b', 3, 0, 3, 1), Task('c', 3, 0, 5, 1)):
            q.insert(task)
        q.change_priority('a', 5)
        self.assertEqual(q.extract_max().task_id, 'a')
        q.change_priority('c', 0)
        self.assertEqual(q.extract_max().task_id, 'b')
        self.assertEqual(q.extract_max().task_id, 'c')
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError): q.extract_max()
        with self.assertRaises(KeyError): q.change_priority('missing', 1)

    def test_duplicate_id_and_scheduler(self):
        q = PriorityQueue(); q.insert(Task('a', 1, 0, 3, 1))
        with self.assertRaises(ValueError): q.insert(Task('a', 2, 0, 3, 1))
        results = simulate([Task('a', 1, 0, 5, 3), Task('b', 4, 1, 3, 1)])
        self.assertEqual([(r[0], r[1], r[2]) for r in results], [('a', 0, 3), ('b', 3, 4)])


if __name__ == '__main__': unittest.main()
