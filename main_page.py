import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import font


class MainPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.logo_image = tk.PhotoImage(file='./assets/logo.png')
        self.label = ttk.Label(self, image=self.logo_image)
        self.label.pack()

        intro_text = (
            "Welcome to the GUI application which will help you perfect your Morse code skills! "
            "The technique of learning Morse code used in the app was created by American memory "
            "athlete Nelson Dellis. The application has different learning modes. Please select one "
            "according to your needs and let's have some fun."
        )
        self.intro_label = ttk.Label(self, text=intro_text, wraplength=450, justify="center")
        self.intro_label.pack()

        youtube_url = "https://www.youtube.com/watch?v=D8tPkb98Fkk"
        youtube_label_text = "Before doing the exercises, please watch Nelson Dellis educational YouTube video!"
        self.youtube_label = HyperlinkLabel(self, text=youtube_label_text, link_url=youtube_url)
        self.youtube_label.pack()

        self.row_frame = ttk.Frame(self)
        self.row_frame.pack()

        self.mode_label = ttk.Label(self.row_frame, text="Select the mode of learning Morse code:")
        self.mode_label.pack(side="left")

        self.options = ["Frequency method", "Phrase method", "Letter to code practice", "Code to letter practice"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.row_frame, textvariable=self.selected_option, values=self.options, state="readonly")
        self.dropdown.pack(side="left")
        self.selected_option.set("Frequency method")

        self.button = ttk.Button(self.row_frame, text="Let's go", command=self.handle_option_selection)
        self.button.pack(side="left")

    def handle_option_selection(self):
        selected_option = self.selected_option.get()
        self.switch_callback(selected_option)


class HyperlinkLabel(tk.Label):
    def __init__(self, parent, text, link_url):
        super().__init__(parent, text=text, cursor="hand2", foreground="blue")
        self.link_url = link_url
        self.bind("<Button-1>", self.open_link)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.normal_font = self.cget("font")
        self.hover_font = font.Font(self, self.normal_font)
        self.hover_font.configure(underline=True)

    def open_link(self, _):
        webbrowser.open_new(self.link_url)

    def on_enter(self, _):
        self.configure(font=self.hover_font)

    def on_leave(self, _):
        self.configure(font=self.normal_font)
