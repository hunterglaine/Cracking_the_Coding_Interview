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


### 2.5 Sum List

# Loop through each linked list (function?)
        # Add the string of each value to a string
        # Add the two ints of those strings
        # Loop through that string
        # Create a new node for each number in the string, starting with first (which points to none)
        # point each succesive num at the previously created node
        # Return the last node created
        def traverse_ll(node):
            ll_str = ""
            while node:
                ll_str += str(node.val)
                node = node.next
                
            ll_list = list(ll_str)
            ll_list.reverse()
            return "".join(ll_list)
        
        num_1 = traverse_ll(l1)
        num_2 = traverse_ll(l2)
        
        result_num = str(int(num_1) + int(num_2))
        next = None
        for num in result_num:
            new_node = ListNode(int(num), next)
            next = new_node
        return new_node


### Reverse Linked List

def reverseList(self, head: ListNode) -> ListNode:
        
    # set prev to None
    # set h to head
    # while h does not equal None
    #   set node to h
    #   set h to h.next
    #   if h is not None
    #       set head to h
    #   set node.next to prev
    #   set prev to node
    # return head

    prev = None
    h = head

    while h != None:
        node = h
        h = h.next
        if h != None:
            head = h
        node.next = prev
        prev = node
    return head

    # Testing to see if commits appear



