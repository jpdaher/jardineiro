
import customtkinter as ctk
from screens.MainScreen import MainScreen


def main():
    # Configurar o modo de aparência (light ou dark)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Criar a janela principal
    app = ctk.CTk()
    app.title("Jardineiro")
    app.geometry("1920x1080")

    main_screen = MainScreen(app)
    main_screen.pack(fill="both", expand=True)

    app.mainloop()


if __name__ == "__main__":
    main()
