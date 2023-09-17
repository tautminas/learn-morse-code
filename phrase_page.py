import tkinter as tk
from tkinter import ttk
import re
import random


class PhrasePage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)

        self.hide_show_button = ttk.Button(self, text="Hide info", command=self.hide_info)

        self.table_label = ttk.Label(self, text="Table of phrase method:")

        style = ttk.Style()
        style.configure("Header.TLabel", background="lightgray")
        self.table_frame = ttk.Frame(self)

        headers = ["Letter", "Phrase", "Morse code"]
        for col, header_text in enumerate(headers):
            header_label = ttk.Label(self.table_frame, text=header_text, relief=tk.RIDGE, style="Header.TLabel")
            header_label.grid(row=0, column=col)

        self.table_data = [
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

        self.phrase_dict = {}
        self.code_dict = {}
        for row in self.table_data:
            letter = row[0]
            phrase = row[1]
            code = row[2]
            self.phrase_dict[letter] = phrase
            self.code_dict[letter] = code

        for row, row_data in enumerate(self.table_data):
            for col, cell_data in enumerate(row_data):
                cell_label = ttk.Label(self.table_frame, text=cell_data, relief=tk.RIDGE)
                cell_label.grid(row=row + 1, column=col)

        self.row_frame = ttk.Frame(self)

        self.random_letter = None
        self.pick_random_letter()
        self.test_label = ttk.Label(self.row_frame, text=f"Write the phrase for a letter {self.random_letter}:")

        self.entry = tk.Entry(self.row_frame, width=32)
        self.entry.insert(0, "Memorable phrase")
        self.entry.config(fg="gray")
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_entry_leave)

        self.test_button = ttk.Button(self.row_frame, text="Test answer", command=self.check_answer)

        self.show_answer_button = ttk.Button(self.row_frame, text="Show answer", command=self.set_entry_text)

        self.answer_label = ttk.Label(self, text="Your answer is...")

        self.pack_elements()



    def pick_random_letter(self):
        random_letter_choice = random.choice(self.table_data)[0]
        while random_letter_choice == self.random_letter:
            random_letter_choice = random.choice(self.table_data)[0]
        self.random_letter = random_letter_choice

    def pack_elements(self):
        self.button.pack(anchor="w")
        self.hide_show_button.pack()
        self.table_label.pack()
        self.table_frame.pack()
        self.test_label.pack(side="left")
        self.entry.pack(side="left")
        self.test_button.pack(side="left")
        self.show_answer_button.pack(side="left")
        self.row_frame.pack()
        self.answer_label.pack()

    def forget_elements(self):
        self.button.pack_forget()
        self.hide_show_button.pack_forget()
        self.table_label.pack_forget()
        self.table_frame.pack_forget()
        self.test_label.pack_forget()
        self.entry.pack_forget()
        self.test_button.pack_forget()
        self.show_answer_button.pack_forget()
        self.row_frame.pack_forget()
        self.answer_label.pack_forget()

    def pack_non_info_elements(self):
        self.button.pack(anchor="w")
        self.hide_show_button.pack()
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
        letter = self.random_letter
        phrase = self.phrase_dict[letter]
        self.entry.delete(0, "end")
        self.entry.insert(0, phrase)
        self.entry.config(fg='black')

    def check_answer(self):
        letter = self.random_letter
        phrase = self.phrase_dict[letter]
        input_answer = re.sub(r'[^a-zA-Z]', '', self.entry.get()).upper()
        real_answer = re.sub(r'[^a-zA-Z]', '', phrase).upper()
        if input_answer == real_answer:
            self.answer_label.config(text=f'Your answer is right. The phrase of letter {letter} really is "{phrase}".', foreground="green")
        else:
            self.answer_label.config(text=f'Your answer is wrong. The phrase of letter {letter} actually is "{phrase}".', foreground="red")
        self.pick_random_letter()
        self.test_label.config(text=f"Write the phrase for a letter {self.random_letter}:")

    def hide_info(self):
        current_text = self.hide_show_button.cget("text")
        new_text = "Hide info" if current_text == "Show info" else "Show info"
        self.hide_show_button.config(text=new_text)

        self.forget_elements()
        if current_text == "Hide info":
            self.pack_non_info_elements()
        else:
            self.pack_elements()