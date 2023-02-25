import unittest

from utils.main import Node, Stack

class Test_func(unittest.TestCase):
    def test_push(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertEqual(node.nextnode, None)

    def test_stack_push(self):
        stack = Stack()
        self.assertEqual(stack.push('data3'), print(stack.top.data))
        self.assertEqual(stack.push(''), None)

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        self.assertEqual(print(stack.top), None)

    def test_stack_pop_2(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')

if __name__ == '__main__':
    unittest.main()
