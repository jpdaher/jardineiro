import customtkinter as ctk
from PIL import Image, ImageTk
from components.Frame import Frame
from components.NavBar import NavBar
from components.CustomButton import CustomButton
from components.CustomEntry import CustomEntry
from components.Card import Card
from modules.TxtParser import parse_tree
from modules.TreeView import node_to_nx, visualize_tree, mark_node
from modules.TreeWrapper import TreeWrapper


class ViewScreen(ctk.CTkFrame):
    def __init__(self, parent, file):
        super().__init__(parent)
        self.root = parse_tree(file)
        self.tree = TreeWrapper(self.root)
        self.navbar = NavBar(self, frame_class=ViewScreen,
                             fg_color=["#FFFFFF", "#1A1A1A"])
        self.navbar.pack(side="top", fill="x")

        self.image_frame = Frame(
            self,
            fg_color=["#F0F0F0", "#1A1A1A"]
        )
        self.image_frame.pack(side="left", fill="both",
                              expand=True, padx=10, pady=10)

        graph_view = visualize_tree(node_to_nx(self.root))

        pil_image = Image.open(graph_view)
        self.image = ImageTk.PhotoImage(pil_image)

        image_label = ctk.CTkLabel(self.image_frame, image=self.image, text="")
        image_label.pack(padx=10, pady=10, expand=True)

        self.frame = Frame(
            self,
            width=450,
            height=450,
            corner_radius=20,
            fg_color=["#FFFFFF", "#1A1A1A"]
        )
        self.frame.pack(side="right", fill="y", padx=10, pady=10)

        total_nodes = Card(self.frame, name="Nós",
                           value=self.tree.count_nodes())
        total_nodes.pack(padx=20, pady=20)

        non_leaves_nodes = Card(
            self.frame, name="Nós não folha",
            value=self.tree.count_not_leaves()
        )
        non_leaves_nodes.pack(padx=20, pady=20)

        custom_entry = CustomEntry(
            self.frame, placeholder="Insira o conteúdo do nó"
        )
        custom_entry.pack(pady=0)

        button_frame = Frame(self.frame, fg_color="transparent")
        button_frame.pack(pady=0)

        # Botão para localizar e visualizar
        button_1 = CustomButton(
            button_frame, text="Localizar",
            command=lambda: self.locate_and_visualize(custom_entry)
        )
        button_1.grid(row=0, column=0, padx=5, pady=10)

        button_2 = CustomButton(button_frame, text="Excluir", command=None)
        button_2.grid(row=0, column=1, padx=6)

    def update_image(self, buffer):
        pil_image = Image.open(buffer)
        self.image = ImageTk.PhotoImage(pil_image)
        self.image_frame.children["!ctklabel"].configure(image=self.image)

    def locate_and_visualize(self, entry_widget):
        value_to_locate = int(entry_widget.get())
        located_node = self.tree.locate(value_to_locate)
        if not located_node:
            print(f"Nó com valor '{value_to_locate}' não encontrado.")
            return

        graph = node_to_nx(self.root)
        node_colors = mark_node(graph, highlight_node=located_node.value)
        updated_graph_view = visualize_tree(graph, node_colors=node_colors)

        self.update_image(updated_graph_view)
