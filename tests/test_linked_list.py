import unittest

from utils.linked_list import LinkedList

class Test_func(unittest.TestCase):
    def test_add_in_the_head(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.first.data, {'id': 0})
        self.assertEqual(ll.first.nextnode.data, {'id': 1})
    def test_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.first.data, {'id': 2})
        self.assertEqual(ll.last.data, {'id': 3})

if __name__ == '__main__':
    unittest.main()