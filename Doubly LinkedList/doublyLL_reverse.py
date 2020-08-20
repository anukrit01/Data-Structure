# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linkedlist class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Print the list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # Insertion methods for Doubly Linkedlist
    # Append method
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head

            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    # Prepend method
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Reverse the Doubly Linkedlist
    def reverse(self):
        tmp = None
        curr = self.head

        while curr:
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if tmp:
            self.head = tmp.prev


# Testing
new_dll = DoublyLinkedList()
new_dll.append('A')
new_dll.append('B')
new_dll.append('C')
new_dll.append('D')

print('Original list: ')
new_dll.print_list()

print('List after reverse: ')
new_dll.reverse()
new_dll.print_list()