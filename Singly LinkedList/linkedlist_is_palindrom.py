# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion as append
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Print the list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    # Insertion using prepend
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    # Insertion after a given node
    def after_node(self, pre_node, data):
        if not pre_node:
            print('Previous node does not exist.')
            return
        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    # Checking if the Linkedlist is palindrom
    def is_palindrom_1(self):
        # Solution-1: using of string
        s = ''
        p = self.head
        while p:
            s += self.head.data
            p = p.next
        return s == s[::-1]

    def is_palindrom_2(self):
        # Solution-2: using stack
        s = []
        p = self.head
        while p:
            s.append(p.data)
            p = p.next
        p = self.head

        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True


# Testing
newlist = LinkedList()
newlist.append('R')
newlist.append('A')
newlist.append('C')
newlist.append('E')
newlist.append('C')
newlist.append('A')
newlist.append('R')

newlist.print_list()
print(newlist.is_palindrom_1())

newlist_1 = LinkedList()
newlist_1.append('A')
newlist_1.append('B')
newlist_1.append('C')
print(newlist_1.is_palindrom_2())