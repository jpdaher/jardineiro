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
    print(value)
    if root.value == value:
        return root
    elif not root.children:
        return False
    else:
        for child in root.children:
            result = locate(child, value)
            if result:
                return result
        return False


def count_binary_nodes(root):
    if not root.left and not root.right:
        return 1
    else:
        count = count_binary_nodes(root.left)
        count += 1
        count += count_binary_nodes(root.right)
        return count


def count_binary_not_leaves(root):
    if not root.left and not root.right:
        return 0
    else:
        count = count_binary_nodes(root.left)
        count += 1
        count += count_binary_nodes(root.right)
        return count


def locate_binary(root, value):
    if value < root.value:
        return locate_binary(root.left, value)
    elif value == root.value:
        return root
    else:
        return locate_binary(root.right, value)


def inorder_successor(node):
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    return None


def delete_binary_node(root, value):
    if not root:
        return root

    if value < root.value:
        root.left = delete_binary_node(root.left, value)
    elif value > root.value:
        root.right = delete_binary_node(root.right, value)
    else:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        successor = inorder_successor(root)
        root.value = successor.value
        root.right = delete_binary_node(
            root.right, successor.value)
    return root


def delete_node(root, value):
    """
    Remove um nó com o valor especificado de uma árvore genérica.
    """
    if root.value == value:
        # Se a raiz for o nó a ser removido
        if root.children:
            new_root = root.children[0]
            # Adiciona os outros filhos
            new_root.children.extend(root.children[1:])
            return new_root
        else:
            return None  # A árvore fica vazia

    # Localiza o nó a ser removido
    node_to_remove = locate(root, value)
    if not node_to_remove:
        print(f"Nó com valor '{value}' não encontrado.")
        return root

    print(f"Nó encontrado: {node_to_remove.value}")  # Para debug

    # Função auxiliar para remover o nó
    def remove_from_children(parent):
        for child in parent.children:
            if child.value == value:
                # Remove o nó e conecta seus filhos ao pai
                parent.children = [
                    c for c in parent.children if c != child
                ]
                parent.children.extend(child.children)
                return True
            else:
                # Chama recursivamente
                if remove_from_children(child):
                    return True
        return False

    # Remove o nó da subárvore
    remove_from_children(root)
    return root
