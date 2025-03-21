import customtkinter as ctk
from tkinter import filedialog


class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text, command=None, **kwargs):
        """
        Componente de botão customizado.
        :param parent: O widget pai onde o botão será exibido.
        :param text: Texto a ser exibido no botão.
        :param command: Função a ser executada ao clicar no botão.
        :param kwargs: Outros argumentos personalizados para o botão.
        """
        text_color = kwargs.pop("text_color", "white")
        font = kwargs.pop("font", ("Arial", 16, "bold"))

        super().__init__(parent, text=text, command=command, **kwargs)

        self.configure(
            text_color=text_color,
            corner_radius=10,
            font=font,
        )

    def read_file(self):
        """
        Abre uma janela de seleção de arquivo.
        """
        file_path = filedialog.askopenfilename(title="Selecione um arquivo")
        return file_path

    def load_screen(self, parent, frame_class, file):
        """
        Carrega a nova tela.
        :param parent: O widget pai atual.
        :param frame_class: Classe da nova tela que será carregada.
        :param file: Arquivo selecionado para carregar os dados.
        """
        parent.pack_forget()  # Esconde a tela atual
        new_screen = frame_class(parent.master, file)
        new_screen.pack(fill="both", expand=True)
