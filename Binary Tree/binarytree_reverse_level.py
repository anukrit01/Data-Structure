# Implementing Queue class as helper
class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


# Stack class as helper
class Stack(object):
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ''
        for i in range(len(self.items)):
            s += str(self.items[i].value) + '-'


# Node Class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree Class
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    # Level-order Traversal
    def reverse_level_order(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ''
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + '-'

        return traversal


# Testing
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

print(tree.reverse_level_order(tree.root))