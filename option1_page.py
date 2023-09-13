import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageFilter, ImageTk


class Option1Page(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        self.button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        self.button.grid(row=0, column=0, sticky="w")

        self.row_frame = tk.Frame(self)
        self.row_frame.grid(row=1, column=0, sticky="nsew")
        self.row_frame.grid_rowconfigure(0, weight=1)
        self.row_frame.grid_columnconfigure(0, weight=1)

        self.story_label = ttk.Label(self.row_frame, text="Story to memorize all the alphabet in frequency order:")
        self.story_label.grid(row=0, column=0, sticky="w")

        story_text = (
            "There is an extraterrestrial (E.T.) named IAN. He is remarkably open-minded, and "
            "suddenly he exclaims, 'Mm, SURe.' Ian grabs a can of WD-40, and before using it, "
            "he mutters to himself, 'Kay, GO.' For some inexplicable reason, he employs this oil "
            "to activate a High-Voltage Frequency. Pausing for a moment, he chuckles to himself, "
            "saying 'Lol.' It was quite a humorous experience. Once he completes his experiment, "
            "Ian puts on his pajamas (PJs), prepares for bed, and then climbs into a BoX. "
            "Interestingly, this box is of size (CYZ) Q, which, on this extraterrestrial planet, "
            "happens to be the standard size for all boxes."
        )

        self.text_widget = tk.Text(self.row_frame, wrap=tk.WORD, width=50, height=13)
        self.text_widget.insert("1.0", story_text)
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.tag_configure("highlight", background="yellow")

        def highlight_letters_in_order():
            letters_to_highlight = "ETIANMSURWDKGOHVFLPJBXCYZQ"
            start_index = "1.0"

            for letter in letters_to_highlight:
                start_index = self.text_widget.search(letter, start_index, stopindex="end")
                if not start_index:
                    break
                end_index = self.text_widget.index(f"{start_index}+1c")
                self.text_widget.tag_add("highlight", start_index, end_index)
                start_index = end_index

        highlight_letters_in_order()

        self.text_widget.grid(row=1, column=0, sticky="w")

        self.label2 = ttk.Label(self.row_frame, text="Frequency order: E T I A N M S U R W D K G O H V F L P J B X C Y Z Q")
        self.grid(row=2, column=0, sticky="w")

        self.logo_image = tk.PhotoImage(file='./assets/binary-tree.png')
        self.label = ttk.Label(self.row_frame, image=self.logo_image)
        self.label.grid(row=3, column=0, sticky="w")

        self.hide_show_button = ttk.Button(self, text="Hide info", command=self.hide_info)
        self.hide_show_button.grid(row=4, column=0, sticky="w")

        self.test_label = ttk.Label(self, text="Write :")
        self.test_label.grid(row=5, column=0, sticky="w")

        self.entry = tk.Entry(self, width=30)
        self.entry.insert(0, "Some text to begin with.")
        self.entry.grid(row=6, column=0, sticky="w")

        self.hide_button = ttk.Button(self, text="Test answer", command=self.switch_callback)
        self.hide_button.grid(row=7, column=0, sticky="w")

    def hide_info(self):
        if self.row_frame.winfo_viewable():
            prev_row = self.row_frame.grid_info()["row"]
            prev_column = self.row_frame.grid_info()["column"]
            self.row_frame.grid_forget()

            self.prev_row = prev_row
            self.prev_column = prev_column
        else:
            self.row_frame.grid(row=self.prev_row, column=self.prev_column, sticky="nsew")