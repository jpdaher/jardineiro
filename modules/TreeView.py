import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO

def node_to_nx(root):
    graph = nx.DiGraph()

    def traverse_binary(node):
        """Percorre a árvore se for binária (usando left e right)."""
        if node is None:
            return

        if node.left:
            graph.add_edge(node.value, node.left.value)
            traverse_binary(node.left)

        if node.right:
            graph.add_edge(node.value, node.right.value)
            traverse_binary(node.right)

    def traverse_generic(node):
        """Percorre a árvore se for genérica (usando children)."""
        for child in node.children:
            graph.add_edge(node.value, child.value)
            traverse_generic(child)

    # **Detecta automaticamente o tipo de árvore**
    if hasattr(root, "left") and hasattr(root, "right"):
        traverse_binary(root)  # Se tem left e right, é binária
    elif hasattr(root, "children"):
        traverse_generic(root)  # Se tem children, é genérica
    else:
        raise ValueError("Estrutura de nó desconhecida!")

    return graph


def mark_node(graph, highlight_node):
    node_colors = [
        "red" if node == highlight_node else "lightblue"
        for node in graph.nodes
    ]
    return node_colors

def hierarchical_pos(graph, root=None, width=1.0, vert_gap=1.0, xcenter=0.5, pos=None, level=0):
    """ Cria um layout hierárquico para a árvore binária """
    if pos is None:
        pos = {}
    if root is None:
        root = next(iter(graph.nodes))  # Pega o primeiro nó como raiz

    pos[root] = (xcenter, -level * vert_gap)
    children = list(graph.successors(root))
    if len(children) > 0:
        dx = width / max(len(children), 2)
        next_x = xcenter - (width / 2) + (dx / 2)
        for child in children:
            pos = hierarchical_pos(graph, root=child, width=dx, vert_gap=vert_gap,
                                   xcenter=next_x, pos=pos, level=level + 1)
            next_x += dx
    return pos

def visualize_tree(graph, node_colors=None):
    pos = hierarchical_pos(graph)

    # Configura o gráfico
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_size=800,
            node_color=node_colors or "lightblue",
            font_size=12, edge_color="gray")
    plt.title("Visualização da Árvore Binária")

    # Salva no buffer de memória
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return buffer
