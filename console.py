from tkinter import *
from tkinter import ttk


class Console:

    def __init__(self, parent, column, row):
        # Initialize main frame that will contain all widgets
        self.main_frame = ttk.Frame(parent)
        self.main_frame.grid(column=column, row=row, sticky=NSEW)
        self.main_frame.columnconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Initialize the test status label
        self.status_label = ttk.Label(self.main_frame)
        self.status_label.grid(column=0, row=0, sticky=NSEW)

        # Initialize the result label
        self.result_label = ttk.Label(self.main_frame)
        self.result_label.grid(column=1, row=0, sticky=NSEW)
        self.update_result()

        # Initialize the new prompt button
        self.new_prompt_button = ttk.Button(self.main_frame, text='New Prompt')
        self.new_prompt_button.grid(column=2, row=0, sticky=NSEW)

        # Initialize the reset button
        self.reset_button = ttk.Button(self.main_frame, text='Reset')
        self.reset_button.grid(column=3, row=0, sticky=NSEW)

    def update_status(self, status):
        self.status_label.configure(text=f'Status: {status}')

    def update_result(self, speed=None, accuracy=None):
        text = ''
        if speed and accuracy:
            text = f'Speed: {speed} WPM   Accuracy: {accuracy}%'
        self.result_label.configure(text=text)
