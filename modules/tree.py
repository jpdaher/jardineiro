class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add_child(self, value):
        if value < self.value:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinaryNode(value)
        elif value > self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinaryNode(value)
        elif value == self.value:
            pass

# Node utilities
def count_nodes(root_node):
    if not root_node.children:
        return 1
    else:
        count = 1
        for child in root_node.children:
            count += count_nodes(child)
        return count
