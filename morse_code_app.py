import tkinter as tk
from main_page import MainPage
from option1_page import Option1Page
from option2_page import Option2Page


class MorseCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Morse Code")

        self.root.minsize(width=500, height=300)

        self.current_frame = None  # Store the current frame

        self.show_main_page()  # Start with the main page

    def show_main_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = MainPage(self.root, self.show_new_page)

    def show_new_page(self, option):
        if self.current_frame:
            self.current_frame.destroy()

        if option == "Frequency Method":
            self.current_frame = Option1Page(self.root, self.show_main_page)
        elif option == "Phrase Method":
            self.current_frame = Option2Page(self.root, self.show_main_page)

