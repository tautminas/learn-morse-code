from main_page import MainPage
from frequency_page import FrequencyPage
from phrase_page import PhrasePage
from letter_to_code_page import LetterToCodePage
from code_to_letter_page import CodeToLetterPage


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

        if option == "Frequency method":
            self.current_frame = FrequencyPage(self.root, self.show_main_page)
        elif option == "Phrase method":
            self.current_frame = PhrasePage(self.root, self.show_main_page)
        elif option == "Letter to code practice":
            self.current_frame = LetterToCodePage(self.root, self.show_main_page)
        elif option == "Code to letter practice":
            self.current_frame = CodeToLetterPage(self.root, self.show_main_page)
