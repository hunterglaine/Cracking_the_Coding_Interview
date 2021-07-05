import linked_lists
import unittest

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, node):
        if not self.head:
            self.head = node
        else: 
            self.tail.next = node

        self.tail = node


class ListNode:
     def __init__(self, val):
         self.val = val
         self.next = None


ll = LinkedList()
ll.add_node(ListNode(1))
ll.add_node(ListNode(2))
ll.add_node(ListNode(2))
ll.add_node(ListNode(3))
ll.add_node(ListNode(4))
ll.add_node(ListNode(4))
ll.add_node(ListNode(4))
ll.add_node(ListNode(5))
ll.add_node(ListNode(6))

# class MyAppUnitTestCase(unittest.TestCase):

#     def test_remove_dups(self):
#         self.assertEqual(linked_lists.remove_dups(ll.head), "my%20web%20site
