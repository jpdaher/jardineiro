
import tkinter as tk


class CustomEntry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent)
        self.config()
