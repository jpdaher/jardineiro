from modules.TreeUtils import count_nodes, count_binary_nodes, count_not_leaves, count_binary_not_leaves, locate, locate_binary, remove_binary_node


class TreeWrapper:
    def __init__(self, root):
        self.root = root
        self.is_binary = hasattr(root, 'left') and hasattr(root, 'right')

    def count_nodes(self):
        if self.is_binary:
            return count_binary_nodes(self.root)
        else:
            return count_nodes(self.root)

    def count_not_leaves(self):
        if self.is_binary:
            return count_binary_not_leaves(self.root)
        else:
            return count_not_leaves(self.root)

    def locate(self, value):
        if self.is_binary:
            return locate_binary(self.root, value)
        else:
            return locate(self.root, value)

    def remove_node(self, value):
        if self.is_binary:
            node = self.locate(value)
            if node:
                remove_binary_node(self.root, node)
            else:
                return False
        else:
            pass
