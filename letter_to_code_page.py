import tkinter as tk
from tkinter import ttk
import random


class LetterToCodePage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.codes_dict = {'A': '• ─', 'B': '─ • • •', 'C': '─ • ─ •', 'D': '─ • •', 'E': '•', 'F': '• • ─ •',
                           'G': '─ ─ •', 'H': '• • • •', 'I': '• •', 'J': '• ─ ─ ─', 'K': '─ • ─', 'L': '• ─ • •',
                           'M': '─ ─', 'N': '─ •', 'O': '─ ─ ─', 'P': '• ─ ─ •', 'Q': '─ ─ • ─', 'R': '• ─ •',
                           'S': '• • •', 'T': '─', 'U': '• • ─', 'V': '• • • ─', 'W': '• ─ ─', 'X': '─ • • ─',
                           'Y': '─ • ─ ─', 'Z': '─ ─ • •'}
        self.letters = list(self.codes_dict.keys())
        self.random_letter = None
        self.pick_random_letter()

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        self.button.pack(anchor="w")

        self.info_label = ttk.Label(self, text="Practice converting letters to Morse code. If you find it difficult it is recommended to spend some more time in phrase method mode. I believe in you!", wraplength=500, justify="center")
        self.info_label.pack()

        self.button_row_frame = ttk.Frame(self)
        self.dot_button = ttk.Button(self.button_row_frame, text="•", command=self.add_dot)
        self.dot_button.pack(side="left")
        self.dash_button = ttk.Button(self.button_row_frame, text="─", command=self.add_dash)
        self.dash_button.pack(side="left")
        self.delete_button = ttk.Button(self.button_row_frame, text="Delete", command=self.remove_answer)
        self.delete_button.pack(side="left")
        self.button_row_frame.pack()

        self.row_frame = ttk.Frame(self)
        self.test_label = ttk.Label(self.row_frame, text=f"Write the code for a letter {self.random_letter}:")
        self.test_label.pack(side="left")
        self.entry = tk.Entry(self.row_frame, width=10, state=tk.DISABLED)
        self.entry.pack(side="left")
        self.check_button = ttk.Button(self.row_frame, text="Test answer", command=self.check_answer)
        self.check_button.pack(side="left")

        self.row_frame.pack()

        self.answer_label = ttk.Label(self, text="Your answer is...")
        self.answer_label.pack()

    def add_dot(self):
        self.entry.config(state=tk.NORMAL)
        if len(self.entry.get()) == 0:
            self.entry.insert(tk.END, "•")
        else:
            self.entry.insert(tk.END, " •")
        self.entry.config(state=tk.DISABLED)

    def add_dash(self):
        self.entry.config(state=tk.NORMAL)
        if len(self.entry.get()) == 0:
            self.entry.insert(tk.END, "─")
        else:
            self.entry.insert(tk.END, " ─")
        self.entry.config(state=tk.DISABLED)

    def remove_answer(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.DISABLED)

    def pick_random_letter(self):
        random_letter_choice = random.choice(self.letters)
        while random_letter_choice == self.random_letter:
            random_letter_choice = random.choice(self.letters)
        self.random_letter = random_letter_choice

    def check_answer(self):
        letter = self.random_letter
        input_answer = self.entry.get()
        real_answer = self.codes_dict[letter]
        if input_answer == real_answer:
            self.answer_label.config(text=f'Your answer is right. The code of letter {letter} really is "{real_answer}".',
                                     foreground="green")
        else:
            self.answer_label.config(
                text=f'Your answer is wrong. The phrase of letter {letter} actually is "{real_answer}".', foreground="red")
        self.pick_random_letter()
        self.test_label.config(text=f"Write the phrase for a letter {self.random_letter}:")
        self.remove_answer()
