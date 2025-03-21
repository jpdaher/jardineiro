import customtkinter as ctk
from PIL import Image, ImageTk
from components.Frame import Frame
from components.Card import Card
from components.CustomButton import CustomButton
from components.CustomEntry import CustomEntry
from components.NavBar import NavBar
from modules.TreeWrapper import TreeWrapper
from modules.TxtParser import parse_tree
from modules.TreeView import node_to_nx, visualize_tree, mark_node


class ViewScreen(ctk.CTkFrame):
    def __init__(self, parent, file):
        super().__init__(parent)

        # Inicializa a árvore e os dados
        self.root = parse_tree(file)
        self.tree = TreeWrapper(self.root)

        # Criação da barra de navegação
        self.navbar = NavBar(self, frame_class=ViewScreen,
                             fg_color=["#FFFFFF", "#1A1A1A"])
        self.navbar.pack(side="top", fill="x")

        # Frame de exibição da imagem (visualização da árvore)
        self.image_frame = Frame(self, fg_color=["#F0F0F0", "#1A1A1A"])
        self.image_frame.pack(side="left", fill="both",
                              expand=True, padx=10, pady=10)

        # Gera a visualização inicial da árvore
        graph_view = visualize_tree(node_to_nx(self.root))
        pil_image = Image.open(graph_view)
        self.image = ImageTk.PhotoImage(pil_image)

        self.image_label = ctk.CTkLabel(
            self.image_frame, image=self.image, text="")
        self.image_label.pack(padx=10, pady=10, expand=True)

        # Frame de controles e informações
        self.frame = Frame(self, width=450, height=450,
                           corner_radius=20, fg_color=["#FFFFFF", "#1A1A1A"])
        self.frame.pack(side="right", fill="y", padx=10, pady=10)

        # Criação dos cards com informações dinâmicas
        self.total_nodes_card = Card(
            self.frame, name="Nós", value=self.tree.count_nodes())
        self.total_nodes_card.pack(padx=20, pady=20)

        self.non_leaves_nodes_card = Card(
            self.frame, name="Nós não folha", value=self.tree.count_not_leaves()
        )
        self.non_leaves_nodes_card.pack(padx=20, pady=20)

        # Campo de entrada de texto para o usuário
        custom_entry = CustomEntry(
            self.frame, placeholder="Insira o conteúdo do nó")
        custom_entry.pack(pady=0)

        # Botões de ação
        button_frame = Frame(self.frame, fg_color="transparent")
        button_frame.pack(pady=0)

        # Botão para localizar e visualizar um nó
        button_1 = CustomButton(
            button_frame, text="Localizar", command=lambda: self.locate_and_visualize(custom_entry)
        )
        button_1.grid(row=0, column=0, padx=5, pady=10)

        # Botão para excluir um nó
        button_2 = CustomButton(
            button_frame, text="Excluir", command=lambda: self.delete_and_visualize(custom_entry)
        )
        button_2.grid(row=0, column=1, padx=6)

    def update_image(self, buffer):
        """
        Atualiza a imagem exibida no frame com base em um buffer.
        """
        pil_image = Image.open(buffer)
        self.image = ImageTk.PhotoImage(pil_image)
        self.image_label.configure(image=self.image)

    def update_cards(self):
        """
        Atualiza os valores exibidos nos cards dinamicamente.
        """
        # Atualiza os valores nos cards com base no estado atual da árvore
        self.total_nodes_card.update_value(self.tree.count_nodes())
        self.non_leaves_nodes_card.update_value(self.tree.count_not_leaves())

    def locate_and_visualize(self, entry_widget):
        """
        Localiza e destaca um nó na visualização da árvore.
        """
        try:
            value_to_locate = int(entry_widget.get())
        except ValueError:
            print("Erro: Insira um número válido.")
            return

        located_node = self.tree.locate(value_to_locate)
        if not located_node:
            print(f"Nó com valor '{value_to_locate}' não encontrado.")
            return

        # Destaca o nó localizado na visualização
        graph = node_to_nx(self.root)
        node_colors = mark_node(graph, highlight_node=located_node.value)
        updated_graph_view = visualize_tree(graph, node_colors=node_colors)

        # Atualiza a visualização da árvore
        self.update_image(updated_graph_view)

    def delete_and_visualize(self, entry_widget):
        """
        Remove um nó e atualiza a visualização e os cards.
        """
        try:
            value_to_delete = int(entry_widget.get())
        except ValueError:
            print("Erro: Insira um número válido.")
            return

        # Remove o nó da árvore
        self.tree.remove_node(value_to_delete)

        # Atualiza a visualização da árvore após a exclusão
        graph = node_to_nx(self.root)
        updated_graph_view = visualize_tree(graph)
        self.update_image(updated_graph_view)

        # Atualiza os valores nos cards
        self.update_cards()
