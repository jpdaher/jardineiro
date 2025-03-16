
import tkinter as tk
from Styles import ENTRY_STYLE


class CustomEntry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(**ENTRY_STYLE)
