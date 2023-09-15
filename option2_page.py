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

        self.table_label = ttk.Label(self, text="Table of phrase method:")
        self.table_label.pack()

        style = ttk.Style()
        style.configure("Header.TLabel", background="lightgray")
        table_frame = ttk.Frame(self)
        table_frame.pack()

        headers = ["Letter", "Phrase", "Morse code"]
        for col, header_text in enumerate(headers):
            header_label = ttk.Label(table_frame, text=header_text, relief=tk.RIDGE, style="Header.TLabel")
            header_label.grid(row=0, column=col)

        table_data = [
            ["A", "A-part", "• ─"],
            ["B", "Bob is the man", "─ • • •"],
            ["C", "Co-ca Co-la", "─ • ─ •"],
            ["D", "Dog did it", "─ • •"],
            ["E", "Eh?", "•"],
            ["F", "Fetch a fire man", "• • ─ •"],
            ["G", "Good gra-vy", "─ ─ •"],
            ["H", "Hi-pi-ty-hop", "• • • •"],
            ["I", "I bid", "• •"],
            ["J", "In Jaws Jaws Jaws", "• ─ ─ ─"],
            ["K", "Kang-a-roo", "─ • ─"],
            ["L", "Los An-ge-les", "• ─ • •"],
            ["M", "Mmmm Mmmm", "─ ─"],
            ["N", "Nu-dist", "─ •"],
            ["O", "Oh my God", "─ ─ ─"],
            ["P", "A poo-py smell", "• ─ ─ •"],
            ["Q", "God save the queen", "─ ─ • ─"],
            ["R", "Ro-ta-tion", "• ─ •"],
            ["S", "Si si si", "• • •"],
            ["T", "Tall", "─"],
            ["U", "U-ni-form", "• • ─"],
            ["V", "Vic-to-ry, vee", "• • • ─"],
            ["W", "The World War", "• ─ ─"],
            ["X", "X marks the spot", "─ • • ─"],
            ["Y", "You're a cool dude", "─ • ─ ─"],
            ["Z", "Zinc zoo kee-per", "─ ─ • •"],
        ]

        for row, row_data in enumerate(table_data):
            for col, cell_data in enumerate(row_data):
                cell_label = ttk.Label(table_frame, text=cell_data, relief=tk.RIDGE)
                cell_label.grid(row=row + 1, column=col)

        self.row_frame = ttk.Frame(self)

        self.test_label = ttk.Label(self.row_frame, text="Write the phrase for a letter ?:")

        self.entry = tk.Entry(self.row_frame, width=32)
        self.entry.insert(0, "Memorable phrase")
        self.entry.config(fg="gray")
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_entry_leave)

        self.test_button = ttk.Button(self.row_frame, text="Test answer", command=self.check_answer)

        self.show_answer_button = ttk.Button(self.row_frame, text="Show answer", command=self.set_entry_text)

        self.answer_label = ttk.Label(self, text="Your answer is...")

        self.test_label.pack(side="left")
        self.entry.pack(side="left")
        self.test_button.pack(side="left")
        self.show_answer_button.pack(side="left")
        self.row_frame.pack()
        self.answer_label.pack()

    def on_entry_click(self, event):
        if self.entry.get() == "Memorable phrase":
            self.entry.delete(0, "end")
            self.entry.config(fg='black')

    def on_entry_leave(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Memorable phrase")
            self.entry.config(fg='gray')

    def set_entry_text(self):
        self.entry.delete(0, "end")
        self.entry.insert(0, "ETIANMSURWDKGOHVFLPJBXCYZQ")
        self.entry.config(fg='black')

    def check_answer(self):
        answer = re.sub(r'[^a-zA-Z]', '', self.entry.get()).upper()
        if answer == "ETIANMSURWDKGOHVFLPJBXCYZQ":
            self.answer_label.config(text="Your answer is correct! Don't forget to celebrate.", foreground="green")
        else:
            self.answer_label.config(text="Your answer is wrong. But I believe in you! ", foreground="red")