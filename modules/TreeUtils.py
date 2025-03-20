def count_nodes(root):
    if not root.children:
        return 1
    else:
        count = 1
        for child in root.children:
            count += count_nodes(child)
        return count

def count_not_leaves(root):
    if not root.children:
        return 0
    else:
        count = 1 
        for child in root.children:
            count += count_not_leaves(child)
        return count

def locate(root, value):
    if root.value == value:
        return root
    elif not root.children:
        return False
    else:
        for child in root.children:
            locate(child, value)

def count_binary_nodes(root):
    if not root.left && not root.right:
        return 1
    else:
        count = count_binary_nodes(root.left)
        count ++
        count += count_binary_nodes(root.right)
        return count

def count_binary_not_leaves(root):
    if not root.left && not root.right:
        return 0
    else:
        count = count_binary_nodes(root.left)
        count++
        count += count_binary_nodes(root.right)
        return count

def locate_binary(root, value):
    if value < root.value:
        return locate_binary(root.left, value)
    elif value == root.value:
        return root
    else return locate_binary(root.right, value)

def remove_binary_node(root, node):
    pass
