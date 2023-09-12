import tkinter as tk
from tkinter import ttk


class Option1Page(tk.Frame):
    def __init__(self, parent, switch_callback):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.switch_callback = switch_callback

        button = ttk.Button(self, text="Back to Main Page", command=self.switch_callback)
        button.pack()

        label = ttk.Label(self, text="Story to memorize all the alphabet in frequency order:")
        label.pack()

        story_text = (
            "There is E.T. and his name happens to be Ian. He is very open-minded and suddenly he says 'Mm, sure'."
            " He gets some WD-40 and before he does something with it he says to himself out loud 'Kay, go'."
            " For some reason, he uses that oil to turn on some high voltage frequency. He pauses for a second,"
            " and says to himself 'L-O-L'. It was a funny experience. Once that's all done, he puts on his PJs,"
            " gets ready for bed, gets inside a box. The box happens to be size (CYZ) Q. Q is the size of all boxes"
            " in this extraterrestrial planet."
        )

        self.text_widget = tk.Text(self, wrap=tk.WORD, width=50, height=11)
        # self.text_widget.pack()
        self.text_widget.insert("1.0", story_text)
        self.text_widget.config(state=tk.DISABLED)
        # Create a tag for highlighting
        self.text_widget.tag_configure("highlight", background="yellow")

        # Highlight specific characters or text
        self.text_widget.tag_add("highlight", "1.6", "1.7")  # Example: Highlight the letter 'E'
        self.text_widget.tag_add("highlight", "1.9", "1.11")  # Example: Highlight the word 'his'

        self.text_widget.pack()

        label2 = ttk.Label(self, text="Frequency order: E T I A N M S U R W D K G O H V F L P J B C Y Z Q")
        label2.pack()

        hide_button = ttk.Button(self, text="Hide info", command=self.switch_callback)
        hide_button.pack()

        test_label = ttk.Label(self, text="Story to memorize all the alphabet in frequency order:")
        test_label.pack()

        entry = tk.Entry(self, width=30)
        entry.insert(0, "Some text to begin with.")  # Use 0 to specify the position to insert text
        entry.pack()


