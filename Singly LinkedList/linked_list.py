
#Simple implementation of a Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

head = Node(2)
head.next = Node(1)

#print(head.value)
#print(head.next.next)

#Adding some more nodes to the list'
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

#Traversing the list
def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

print_linked_list(head)
'''

#Creating a linked list efficiently
def create_linked_list(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head         # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(value)     # attach the new node to the `next` of tail
            tail = tail.next            # update the tail
    
    return head

input_list = [6,7,5,2,3,4]
print(create_linked_list(input_list))
