from tkinter import *
from tkinter import ttk
from passages import passages


class Prompt:

    def __init__(self, parent, column, row):
        # Initialize main frame that will contain all widgets
        self.main_frame = ttk.Frame(parent)
        self.main_frame.grid(column=column, row=row, sticky=NSEW)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Initialize prompt text
        self.text = Text(self.main_frame,
                         width=1,
                         height=1,
                         font=('TkDefaultFont', 16),
                         wrap='word',
                         state='disabled')
        self.text.grid(column=0, row=0, sticky=NSEW)

        self.prompt_idx = -1
        self.set_prompt()

    # Handles the rolling prompt index and presenting the current prompt
    def set_prompt(self, event=None):
        # Increment prompt index based on number of passages
        self.prompt_idx = (self.prompt_idx + 1) % len(passages)

        # Write passage content into prompt text area
        self.text.configure(state='normal')
        self.text.delete('1.0', END)
        self.text.insert('1.0', self.get_prompt_content())
        self.text.configure(state='disabled')

    # Returns the content of the current prompt passage
    def get_prompt_content(self):
        return passages[self.prompt_idx][0]

    # Returns the character count of the current prompt passage
    def get_prompt_character_count(self):
        return len(passages[self.prompt_idx][0])

    # Returns the word count of the current prompt passage
    def get_prompt_word_count(self):
        return passages[self.prompt_idx][1]
