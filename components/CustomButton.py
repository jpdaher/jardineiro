
import customtkinter as ctk


class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text, command=None, **kwargs):
        """
        Componente de botão customizado.
        :param parent: O widget pai onde o botão será exibido.
        :param text: Texto a ser exibido no botão.
        :param command: Função a ser executada ao clicar no botão.
        :param kwargs: Outros argumentos personalizados para o botão.
        """
        # Configurando os argumentos padrão caso não sejam passados
        text_color = kwargs.pop("text_color", "white")
        font = kwargs.pop("font", ("Arial", 16, "bold"))

        # Chamando o método inicializador da superclasse
        super().__init__(parent, text=text, command=command, **kwargs)

        # Aplicando o estilo personalizado (valores padrão ou passados)
        self.configure(
            text_color=text_color,
            corner_radius=10,
            font=font,
        )
