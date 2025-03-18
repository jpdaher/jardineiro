from tree import Node, BinaryNode

def parse_tree(filename):
    root = None
    stack = []
    file = open(filename, "r")
    lines = file.readlines()

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

parse_tree("tree.txt")



