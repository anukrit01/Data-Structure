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

    # length of LinkedList using iterative method
    def length_iterative(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    # Length of Linkedlist using recursive method
    def length_recurs(self, node):
        if node is None:
            return 0
        
        return 1 + self.length_recurs(node.next)



# Testing
newlist = LinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.prepend('D')
newlist.after_node(newlist.head.next, 'E')
print(newlist.length_iterative())

newlist.print_list()
print('Length by recursion: ', newlist.length_recurs(newlist.head))