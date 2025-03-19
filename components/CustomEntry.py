
import customtkinter as ctk


class CustomEntry(ctk.CTkEntry):
    def __init__(self, parent, placeholder="Digite aqui...", width=300, height=40, corner_radius=10, **kwargs):
        """
        CustomEntry: Um campo de entrada personalizado.

        :param parent: O widget pai.
        :param placeholder: Texto exibido como placeholder.
        :param width: Largura do campo.
        :param height: Altura do campo.
        :param corner_radius: Raio das bordas arredondadas.
        :param kwargs: Argumentos adicionais para personalização.
        """
        super().__init__(parent,
                         placeholder_text=placeholder,
                         width=width,
                         height=height,
                         corner_radius=corner_radius,
                         fg_color="#F3F4F6",
                         text_color="#000000",
                         **kwargs)

    def get(self):
        """
        Retorna o texto inserido no campo.
        """
        return super().get()

    def set(self, text):
        """
        Define o texto no campo de entrada.
        """
        self.delete(0, "end")
        self.insert(0, text)
