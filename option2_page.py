import tkinter as tk
from tkinter import ttk


class Option2Page(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        self.button.pack(anchor="w")

        self.hide_show_button = ttk.Button(self, text="Hide info", command=self.switch_callback)
        self.hide_show_button.pack()

        self.explanatory_label = ttk.Label(self, text="Explanation:")
        self.explanatory_label.pack()

        label = ttk.Label(self, text="This is Option 2 Page")
        label.pack()

