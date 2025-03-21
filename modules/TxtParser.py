from tree import Node, BinaryNode
from TreeUtils import count_nodes, count_not_leaves, locate, count_binary_nodes, count_binary_not_leaves, locate_binary, remove_binary_node

def parse_tree(filename):
    root = None
    stack = []
    file = open(filename, "r")
    lines = file.readlines()

    for line in lines:
        stripped_line = line.rstrip()
        print("stripped line: ", stripped_line) #debug
        level = stripped_line.count("-")
        print("level: ", level) #debug
        value = int(stripped_line.strip("-"))
        print("value: ", value) #debug
        new_node = Node(value)
        print("new node created with value ", value) #debug

        if level == 0:
            root = new_node
            print("root node created") #debug
            stack.append(root)
            print("root node inserted into stack") #debug
        else:
            print("popping stack elements") #debug
            while level < len(stack):
                stack.pop()
            print("stack len now equal to level") #debug
            stack[-1].add_child(new_node)
            print("adding ", new_node.value, " as child of ", stack[-1].value) #debug
            stack.append(new_node)
            print("appending new node to stack") #debug

    print("finished parsing tree, returning root node") #debug

    return root

def parse_binary_tree(filename):
    root = None
    file = open(filename, "r")
    numbers = list(map(int,file.read().split(", ")))
    for number in numbers:
       root.add_child(number)
    return root

node = parse_tree("tree.txt")
print("Number of nodes in the tree: ", count_nodes(node))
print("Number of nodes that are not leaves: ", count_not_leaves(node))



