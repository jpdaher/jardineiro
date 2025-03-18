import customtkinter as ctk
from tkinter import PhotoImage
from components.Frame import Frame
from components.NavBar import NavBar
from components.CustomButton import CustomButton
from screens.ViewScreen import ViewScreen


class MainScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Adicionar a NavBar
        self.navbar = NavBar(self, fg_color=["#FFFFFF", "#1A1A1A"])
        self.navbar.pack(side="top", fill="x")

        # Frame principal
        self.frame = Frame(
            self,
            width=650,
            height=450,
            corner_radius=20,
            fg_color=["#FFFFFF", "#1A1A1A"]
        )
        self.frame.pack(expand=True, fill="none")

        # Adicionar imagem
        self.image = PhotoImage(file="./images/file_not_found.png")
        self.image = self.image.subsample(3, 3)

        image_label = ctk.CTkLabel(self.frame, image=self.image, text="")
        image_label.pack(pady=25)

        # Adicionar título
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

        # Adicionar botão
        button = CustomButton(
            self.frame,
            text="Criar árvore de exemplo",
            command=lambda: self.go_to_screen(ViewScreen),
            width=250,
            height=50,
        )
        button.pack(pady=50)

    def go_to_screen(self, frame_class):
        self.pack_forget()  # Esconde a tela atual
        # Substitui a tela com nova classe
        view_screen = frame_class(self.master)
        view_screen.pack(fill="both", expand=True)
