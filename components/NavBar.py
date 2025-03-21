
import customtkinter as ctk
from components.Frame import Frame
from components.CustomButton import CustomButton
from tkinter import PhotoImage


class NavBar(Frame):
    def __init__(self, parent, frame_class, **kwargs):
        """
        Classe NavBar com logo no canto esquerdo e botão no canto direito.
        :param parent: O widget pai onde a NavBar será exibida.
        :param frame_class: Classe da tela que será usada ao clicar no botão.
        :param kwargs: Argumentos adicionais para personalização.
        """
        super().__init__(parent, height=60, corner_radius=0, **kwargs)

        self.pack_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_logo()

        # Passa o frame_class ao botão
        self.add_transparent_button(parent, frame_class)

    def add_logo(self):
        """Adiciona a imagem (logo) ao canto esquerdo da NavBar."""
        self.logo = PhotoImage(file="./images/logo.png")
        self.logo = self.logo.subsample(5, 5)

        logo_label = ctk.CTkLabel(self, image=self.logo, text="")
        logo_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    def add_transparent_button(self, parent, frame_class):
        """Adiciona um botão transparente no canto direito da NavBar."""
        transparent_button = CustomButton(
            self,
            text=" Carregar arquivo",
            command=lambda: transparent_button.load_screen(
                parent, frame_class, transparent_button.read_file()),
            width=140,
            height=50,
            fg_color="transparent",
            border_width=2,
            text_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
            border_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
        )
        transparent_button.grid(row=0, column=1, padx=40, pady=5, sticky="e")
