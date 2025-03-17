from tkinter import *
from tkinter import ttk


class Entry:

    def __init__(self, parent, column, row):
        # Initialize main frame that will contain all widgets
        self.main_frame = ttk.Frame(parent)
        self.main_frame.grid(column=column, row=row, sticky=NSEW)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Initialize entry text box
        self.text = Text(self.main_frame,
                         width=1,
                         height=1,
                         font=('TkDefaultFont', 16),
                         wrap='word')
        self.text.grid(column=0, row=0, sticky=NSEW)
        self.reset()

    # Resets the Entry to display the instructions
    def reset(self, event=None):
        self.text.configure(state='normal')
        self.clear()
        self.text.insert('1.0',
                         'Select this box and begin typing the prompt above to start the test.\n'
                         'The test will automatically end when the character count matches the prompt.\n'
                         'Line breaks/carriage returns are not needed. Lines will wrap automatically.')

    # Removes all content from Entry
    def clear(self, event=None):
        self.text.delete('1.0', END)

    def get_entry_content(self):
        return self.text.get('1.0', END)[:-1]  # Remove newline that Tkinter adds

    def disable(self):
        self.text.configure(state='disabled')
