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

    def sum_two_lists(self, newlist):
        p = self.head
        q = newlist.head

        sum_newlist = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_newlist.append(remainder)
            else:
                carry = 0
                sum_newlist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_newlist.print_list()


# Testing
newlist = LinkedList()
newlist.append(1)
newlist.append(2)
newlist.append(3)
newlist.prepend(4)
newlist.after_node(newlist.head.next, 6)

newlist_1 = LinkedList()
newlist_1.append(3)
newlist_1.append(7)
newlist_1.append(5)

newlist.print_list()
newlist_1.print_list()
print(32614 + 573)
newlist.sum_two_lists(newlist_1)