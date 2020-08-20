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

    
    # Deletion By Value
    def delete_node(self, key):

        curr_node = self.head
        
        # Deleting Head Node
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        # Deleting Other node
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None


# Testing
newlist = LinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.prepend('D')
newlist.after_node(newlist.head.next, 'E')
newlist.delete_node('B')
newlist.delete_node('Z')

newlist.print_list()