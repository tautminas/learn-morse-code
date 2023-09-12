import tkinter as tk
from tkinter import ttk
import webbrowser


class MainPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.logo_image = tk.PhotoImage(file='./assets/logo.png')
        label = ttk.Label(self, image=self.logo_image)
        label.pack()

        intro_label = ttk.Label(self, text="Welcome to the GUI application which will help you perfectionize your morse code skills! "
                                           "The technique of learning Morse code which is used in the app is created by American memory athlete Nelson Dellis. "
                                           "Application has different modes of learning. Please select one according to your needs and let's have some fun!", wraplength=400, justify="center")
        intro_label.pack()

        youtube_url = "https://www.youtube.com/watch?v=D8tPkb98Fkk"
        youtube_label_text = "Before doing the exercises, please watch Nelson Dellis educational YouTube video!"
        youtube_label = HyperlinkLabel(self, text=youtube_label_text, link_url=youtube_url)
        youtube_label.pack()

        mode_label = ttk.Label(self, text="Select the mode of learning Morse code:")
        mode_label.pack()

        options = ["Frequency Method", "Phrase Method"]
        self.selected_option = tk.StringVar()
        dropdown = ttk.Combobox(self, textvariable=self.selected_option, values=options, state="readonly")
        dropdown.pack()
        self.selected_option.set("Frequency Method")

        button = ttk.Button(self, text="Let's go", command=self.handle_option_selection)
        button.pack()

    def handle_option_selection(self):
        selected_option = self.selected_option.get()
        self.switch_callback(selected_option)


class HyperlinkLabel(tk.Label):
    def __init__(self, parent, text, link_url):
        super().__init__(parent, text=text, cursor="hand2", foreground="blue", underline=True)
        self.link_url = link_url
        self.bind("<Button-1>", self.open_link)

    def open_link(self, event):
        webbrowser.open_new(self.link_url)