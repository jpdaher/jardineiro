
import customtkinter as ctk
from tkinter import PhotoImage
from components.Frame import Frame
from components.NavBar import NavBar
from components.CustomButton import CustomButton
from components.CustomEntry import CustomEntry
from components.Card import Card
from modules.tree import count_nodes
from modules.TxtParser import parse_tree


class ViewScreen(ctk.CTkFrame):
    def __init__(self, parent, file):
        super().__init__(parent)
        self.root = parse_tree(file)
        # Adicionar a NavBar
        self.navbar = NavBar(self, fg_color=["#FFFFFF", "#1A1A1A"])
        self.navbar.pack(side="top", fill="x")

        self.frame = Frame(
            self,
            width=450,
            height=450,
            corner_radius=20,
            fg_color=["#FFFFFF", "#1A1A1A"]
        )
        self.frame.pack(side="right", fill="y", pady=10, padx=10)

        total_nodes = Card(self.frame, name="Nós",
                           value=count_nodes(self.root))
        total_nodes.pack(padx=20, pady=20)

        non_leaves_nodes = Card(self.frame, name="Nós não folha", value=0)
        non_leaves_nodes.pack(padx=20, pady=20)

        custom_entry = CustomEntry(
            self.frame, placeholder="Insira o conteudo do nó")
        custom_entry.pack(pady=0)

        button_frame = Frame(self.frame, fg_color="transparent")
        button_frame.pack(pady=0)

        button_1 = CustomButton(
            button_frame, text="Localizar", command=None)
        button_1.grid(row=0, column=0, padx=5, pady=10)

        button_2 = CustomButton(
            button_frame, text="Excluir", command=None)
        button_2.grid(row=0, column=1, padx=6)
