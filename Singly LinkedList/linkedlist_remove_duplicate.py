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

    # Remove Duplicate
    def remove_duplicate(self):
        curr = self.head
        prev = None

        duplicates = dict()

        while curr:
            #checking if the node is duplicate
            if curr.data in duplicates:
                #delete that node
                prev.next = curr.next
                curr = None

            #when the node is not duplicate
            else:
                duplicates[curr.data] = 1
                prev = curr
            curr = prev.next


# Testing
newlist = LinkedList()
newlist.append('A')
newlist.append('B')
newlist.append('C')
newlist.prepend('D')
newlist.after_node(newlist.head.next, 'E')
newlist.append('A')
newlist.append('C')
newlist.append('E')

print('The original linked list:')
newlist.print_list()

newlist.remove_duplicate()
print('After removing the duplicates:')
newlist.print_list()