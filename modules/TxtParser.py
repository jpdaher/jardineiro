from modules.tree import Node, BinaryNode
from modules.TreeUtils import count_nodes, count_not_leaves, locate, count_binary_nodes, count_binary_not_leaves, locate_binary


def parse_tree(filename):
    root = None
    stack = []
    file = open(filename, "r")
    content = file.read().strip()
    lines = content.split("\n")

    if "," in content:
        numbers = list(map(int, content.split(", ")))
        root = BinaryNode(numbers[0])
        for number in numbers:
            root.add_child(number)
        return root
    

    for line in lines:
        stripped_line = line.rstrip()
        level = stripped_line.count("-")
        value = int(stripped_line.strip("-"))
        new_node = Node(value)

        if level == 0:
            root = new_node
            stack.append(root)
        else:
            while level < len(stack):
                stack.pop()
            stack[-1].add_child(new_node)
            stack.append(new_node)
    return root


def parse_binary_tree(filename):
    root = None
    file = open(filename, "r")
    numbers = list(map(int, file.read().split(", ")))
    for number in numbers:
        root.add_child(number)
    return root
