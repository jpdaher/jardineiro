import customtkinter as ctk
from tkinter import PhotoImage
from components.Frame import Frame
from components.NavBar import NavBar
from components.CustomButton import CustomButton


class ViewScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Adicionar a NavBar
        self.navbar = NavBar(self, fg_color=["#FFFFFF", "#1A1A1A"])
        self.navbar.pack(side="top", fill="x")

        self.frame = Frame(
            self,
            width=650,
            height=450,
            corner_radius=20,
            fg_color=["#FFFFFF", "#1A1A1A"]
        )
        # Mantém o frame ancorado à direita
        self.frame.pack(side="right", fill="y", pady=10, padx=10)

        title = ctk.CTkLabel(
            self.frame,
            text="Nenhuma árvore carregada",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=0)

        # Adicionar subtítulo
        label = ctk.CTkLabel(
            self.frame,
            text="Carregue um arquivo contendo dados de árvore\n para começar.",
            font=("Arial", 20)
        )
        label.pack(pady=10)
