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

    # Finding Nth node counting from last of linkedlist
    def nth_from_last(self, n):
        total_length = self.length_iterative()

        curr = self.head
        while curr:
            if total_length == n:
                print(curr.data)
                return curr.data
            total_length -= 1
            curr = curr.next
        if curr is None:
            return


# Testing
newlist = LinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.prepend('D')
newlist.after_node(newlist.head.next, 'E')

newlist.print_list()
print('2nd node from last in the linkedlist is: ')
newlist.nth_from_last(2)