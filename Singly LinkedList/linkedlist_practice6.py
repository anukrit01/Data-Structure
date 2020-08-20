# Skip - i Delete - j
'''
Problem Statement

You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

    linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
    i = 2
    j = 3
    Output = 1 2 6 7 11 12

# LinkedList Node class for your reference
'''

class Node:

    def __init__(self, data):

        self.data = data

        self.next = None

# Solution
"""
:param: head - head of linked list
:param: i - first `i` nodes that are to be skipped
:param: j - next `j` nodes that are to be deleted
return - return the updated head of the linked list
"""
'''
The Idea: 
Traverse the Linkedist. Make use of two references - `current` and `previous`.
 - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
 - Delete next `j` nodes. Keep incrementing the `current`.
 - Connect the `previous.next` to the `current`
'''
def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    current = head
    previous = None
    
    # Traverse - Loop untill there are Nodes available in the LinkedList
    while current:
        
        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        '''delete next j nodes'''
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        
        '''Connect the `previous.next` to the `current`''' 
        previous.next = current
    
    # Loop ends
    
    return head