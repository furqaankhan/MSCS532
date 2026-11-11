"""Nonpreemptive priority scheduling with an indexed binary max-heap."""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Task:
    task_id: str
    priority: int
    arrival: int
    deadline: int
    duration: int


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.positions = {}
        self.sequence = 0

    def is_empty(self):
        return not self.heap

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.positions[self.heap[a][2].task_id] = a
        self.positions[self.heap[b][2].task_id] = b

    def _up(self, i):
        while i:
            parent = (i - 1) // 2
            if self.heap[parent][:2] >= self.heap[i][:2]: break
            self._swap(i, parent); i = parent

    def _down(self, i):
        while 2 * i + 1 < len(self.heap):
            child = 2 * i + 1
            if child + 1 < len(self.heap) and self.heap[child + 1][:2] > self.heap[child][:2]:
                child += 1
            if self.heap[i][:2] >= self.heap[child][:2]: break
            self._swap(i, child); i = child

    def insert(self, task):
        if task.task_id in self.positions: raise ValueError('duplicate task ID')
        entry = (task.priority, -self.sequence, task)
        self.sequence += 1
        self.positions[task.task_id] = len(self.heap)
        self.heap.append(entry)
        self._up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty(): raise IndexError('extract from empty queue')
        self._swap(0, len(self.heap) - 1)
        _, _, task = self.heap.pop()
        del self.positions[task.task_id]
        if self.heap: self._down(0)
        return task

    def change_priority(self, task_id, new_priority):
        i = self.positions[task_id]
        old, sequence, task = self.heap[i]
        self.heap[i] = (new_priority, sequence, replace(task, priority=new_priority))
        if new_priority > old: self._up(i)
        elif new_priority < old: self._down(i)


def simulate(tasks):
    """Return (id, start, finish, wait, late) for nonpreemptive jobs."""
    if any(t.arrival < 0 or t.duration <= 0 for t in tasks):
        raise ValueError('arrival must be nonnegative and duration positive')
    if len({t.task_id for t in tasks}) != len(tasks):
        raise ValueError('task IDs must be unique')
    pending = sorted(tasks, key=lambda t: t.arrival)
    queue, results, now, index = PriorityQueue(), [], 0, 0
    while index < len(pending) or not queue.is_empty():
        if queue.is_empty() and now < pending[index].arrival:
            now = pending[index].arrival
        while index < len(pending) and pending[index].arrival <= now:
            queue.insert(pending[index]); index += 1
        task = queue.extract_max()
        start = now
        now += task.duration
        results.append((task.task_id, start, now, start - task.arrival, now > task.deadline))
    return results


if __name__ == '__main__':
    tasks = [Task('A', 2, 0, 6, 3), Task('B', 5, 1, 5, 2),
             Task('C', 3, 2, 7, 1), Task('D', 5, 3, 8, 2),
             Task('E', 1, 10, 13, 2)]
    print('task start finish wait missed_deadline')
    for row in simulate(tasks): print(*row)
