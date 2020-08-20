# Detecting Loops in Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list = None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

def icircular(linked_list):
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

# Creating a loop where the last node points back to the second node

list_with_loop = LinkedList([2, -1, 3, 0, 5])
loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next

node.next = loop_start

print(icircular(list_with_loop))
print(icircular(LinkedList([-4, 7, 2, 5, -1])))