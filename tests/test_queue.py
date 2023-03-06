import unittest

from utils.custom_queue import Queue

class Test_func(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.first.data, 'data1')
        self.assertEqual(queue.first.nextnode.data, 'data2')
        self.assertEqual(queue.last.data, 'data3')
        self.assertEqual(queue.last.nextnode, None)
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.first.data, 'data1')
        self.assertEqual(queue.first.nextnode.data, 'data2')
        self.assertEqual(queue.last.data, 'data3')
        self.assertEqual(queue.last.nextnode, None)


if __name__ == '__main__':
    unittest.main()
