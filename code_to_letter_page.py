import tkinter as tk
from tkinter import ttk
import random


class CodeToLetterPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.codes_dict = {'A': '• ─', 'B': '─ • • •', 'C': '─ • ─ •', 'D': '─ • •', 'E': '•', 'F': '• • ─ •',
                           'G': '─ ─ •', 'H': '• • • •', 'I': '• •', 'J': '• ─ ─ ─', 'K': '─ • ─', 'L': '• ─ • •',
                           'M': '─ ─', 'N': '─ •', 'O': '─ ─ ─', 'P': '• ─ ─ •', 'Q': '─ ─ • ─', 'R': '• ─ •',
                           'S': '• • •', 'T': '─', 'U': '• • ─', 'V': '• • • ─', 'W': '• ─ ─', 'X': '─ • • ─',
                           'Y': '─ • ─ ─', 'Z': '─ ─ • •'}
        self.letters_dict = {value: key for key, value in self.codes_dict.items()}
        self.letters = list(self.codes_dict.keys())
        self.random_letter = None
        self.pick_random_letter()

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        self.button.pack(anchor="w")

        self.info_label = ttk.Label(self, text="Practice converting Morse code to letters. If you find it difficult it is recommended to spend some more time in phrase method mode. I believe in you!", wraplength=500, justify="center")
        self.info_label.pack()

        self.row_frame = ttk.Frame(self)
        self.test_label = ttk.Label(self.row_frame, text=f"Write the letter whose Morse code is {self.codes_dict[self.random_letter]}:")
        self.test_label.pack(side="left")
        self.entry = tk.Entry(self.row_frame, width=5)
        self.entry.pack(side="left")
        self.check_button = ttk.Button(self.row_frame, text="Test answer", command=self.check_answer)
        self.check_button.pack(side="left")
        self.row_frame.pack()

        self.answer_label = ttk.Label(self, text="Your answer is...")
        self.answer_label.pack()

    def pick_random_letter(self):
        random_letter_choice = random.choice(self.letters)
        while random_letter_choice == self.random_letter:
            random_letter_choice = random.choice(self.letters)
        self.random_letter = random_letter_choice

    def check_answer(self):
        pass
