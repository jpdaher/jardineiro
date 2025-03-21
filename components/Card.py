import customtkinter as ctk
from components.Frame import Frame


class Card(Frame):
    def __init__(self, parent, name, value, width=300, height=200, corner_radius=15, **kwargs):
        """
        Componente de Card que exibe um nome e um valor centralizados.

        :param parent: O widget pai.
        :param name: O nome que será exibido no card.
        :param value: O valor que será exibido no card.
        :param width: Largura do card.
        :param height: Altura do card.
        :param corner_radius: Raio das bordas arredondadas.
        :param kwargs: Argumentos adicionais para personalização.
        """
        super().__init__(parent, width=width, height=height,
                         corner_radius=corner_radius,
                         fg_color=["#E0E4E8", "#2D2F34"], **kwargs)

        # Impede que o tamanho do frame seja alterado pelos widgets
        self.pack_propagate(False)
        name_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        # Criação do label para o nome
        self.name_label = ctk.CTkLabel(
            self, text=name, font=("Roboto", 18, "bold"), text_color=name_color)
        # Centraliza o nome no card
        self.name_label.place(relx=0.5, rely=0.4, anchor="center")

        # Criação do label para o valor
        self.value_label = ctk.CTkLabel(
            self, text=value, font=("Roboto", 16))
        # Centraliza o valor no card
        self.value_label.place(relx=0.5, rely=0.6, anchor="center")

    def update_value(self, new_value):
        self.value_label.configure(text=str(new_value))
