import tkinter as tk
from tkinter import ttk


class CodeToLetterPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        self.button.pack(anchor="w")

        self.test_label = ttk.Label(self, text="Test")
        self.test_label.pack()
