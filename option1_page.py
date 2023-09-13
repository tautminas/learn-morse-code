import tkinter as tk
from tkinter import ttk


class Option1Page(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        button.pack()

        story_label = ttk.Label(self, text="Story to memorize all the alphabet in frequency order:")
        story_label.pack()

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

        self.text_widget = tk.Text(self, wrap=tk.WORD, width=50, height=13)
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

        self.text_widget.pack()

        label2 = ttk.Label(self, text="Frequency order: E T I A N M S U R W D K G O H V F L P J B X C Y Z Q")
        label2.pack()

        self.logo_image = tk.PhotoImage(file='./assets/binary-tree.png')
        label = ttk.Label(self, image=self.logo_image)
        label.pack()

        hide_show_button = ttk.Button(self, text="Hide info", command=self.switch_callback)
        hide_show_button.pack()

        test_label = ttk.Label(self, text="Write :")
        test_label.pack()

        entry = tk.Entry(self, width=30)
        entry.insert(0, "Some text to begin with.")
        entry.pack()

        hide_button = ttk.Button(self, text="Test answer", command=self.switch_callback)
        hide_button.pack()
