### 2.1 Remove Dups
# Write code to remove duplicates from an unsorted linked list. 

# Loop through linked list, while the next node is not None
# Keep track of prev and curr
# Put each value in a dictionary
# If the value already exists, remove it by changing prev's next to next next
# Return the head
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


def remove_dups(head):
    nodes = {head.val}
    curr = head.next
    prev = head

    while curr:
        if curr.val in nodes:
            prev.next = prev.next.next
        else:
            nodes.add(curr.val)
            prev = curr
        curr = curr.next
    
    return head


### 2.2 Return Kth to Last
# Implement an algorithm to find the Kth to laast element of a singly linked list.

### 2.3 Delete Middle Node
# Given a node, delete that node. Alter the list in place and return nothing. 

def delete_middle(node):
    curr = node
    nxt = node.next

    while nxt:
        curr.val = nxt.val
        if not nxt.next:
            curr.next = None
        curr = nxt
        nxt = nxt.next



