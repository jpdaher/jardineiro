import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO


def node_to_nx(root):
    graph = nx.DiGraph()

    def traverse(node):
        for child in node.children:
            graph.add_edge(node.value, child.value)
            traverse(child)

    traverse(root)
    return graph


def mark_node(graph, highlight_node):
    node_colors = [
        "red" if node == highlight_node else "lightblue"
        for node in graph.nodes
    ]
    return node_colors


def visualize_tree(graph, node_colors=None):
    pos = nx.planar_layout(graph)

    # Configura o gráfico
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_size=800,
            node_color=node_colors or "lightblue",
            font_size=12)
    plt.title("Visualização da Árvore")

    # Salva no buffer de memória
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    return buffer
