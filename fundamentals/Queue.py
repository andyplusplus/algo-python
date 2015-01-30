__author__ = 'andy'

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)<1: return None
        item = self.queue[0]
        del self.queue[0]
        return item

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

from unittest import TestCase
class Test_Queue(TestCase):
    def test(self):
        que = Queue()
        self.assertTrue(que.isEmpty())
        for i in range(10):
            que.enqueue(i)
        self.assertTrue(que.size()==10)
        self.assertEqual(que.dequeue(), 0)