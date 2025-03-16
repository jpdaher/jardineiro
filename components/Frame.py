
import customtkinter as ctk


class Frame(ctk.CTkFrame):
    def __init__(self, parent, width=300, height=200, corner_radius=15, **kwargs):
        """
        Um Frame simples que permite adicionar widgets.
        :param parent: O widget pai.
        :param width: Largura do frame.
        :param height: Altura do frame.
        :param corner_radius: Raio das bordas arredondadas.
        :param kwargs: Argumentos adicionais para personalização.
        """
        super().__init__(parent, width=width, height=height,
                         corner_radius=corner_radius, **kwargs)

        # Configurar layout interno para acomodar widgets
        # Impede que o tamanho do frame seja alterado pelos widgets
        self.pack_propagate(False)
