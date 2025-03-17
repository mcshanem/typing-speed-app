from tkinter import *
from tkinter import ttk
import tkinter.font as tk_font
from prompt import Prompt
from entry import Entry
from console import Console
from timeit import default_timer as timer
import jellyfish

STATUS_NOT_STARTED = 'Not Started'
STATUS_RUNNING = 'Running'
STATUS_FINISHED = 'Finished'


class App:

    def __init__(self, parent):
        # Initialize testing variables
        self.test_status = STATUS_NOT_STARTED
        self.test_start = None
        self.test_end = None

        # Initialize parent window
        parent.title('Typing Speed App')
        parent.geometry('1000x550')
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        # Initialize main frame that will contain all widgets
        self.main_frame = ttk.Frame(parent)
        self.main_frame.grid(column=0, row=0, sticky=NSEW)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure((0, 1), weight=10)
        self.main_frame.rowconfigure(2, weight=1)

        # Configure fonts and styles
        default_font = tk_font.nametofont('TkDefaultFont')
        default_font.configure(size=16)

        # Create the child sections
        self.prompt = Prompt(self.main_frame, 0, 0)
        self.entry = Entry(self.main_frame, 0, 1)
        self.console = Console(self.main_frame, 0, 2)

        # Set up bindings
        self.entry.text.bind('<FocusIn>', self.entry.clear)
        self.entry.text.bind('<KeyRelease>', self.monitor_test)
        self.console.new_prompt_button.bind('<ButtonRelease-1>', self.prompt.set_prompt)
        self.console.reset_button.bind('<ButtonRelease-1>', self.reset)

        # Pass the status to the console
        self.console.update_status(self.test_status)

    # Handles test start, stop, and monitoring
    def monitor_test(self, event):
        # Start the test on the first keystroke
        if self.test_status == STATUS_NOT_STARTED:
            self.test_status = STATUS_RUNNING
            self.test_start = timer()
        # Monitor for completion of the test while it's running
        if self.test_status == STATUS_RUNNING:
            typed_character_count = len(self.entry.get_entry_content())
            if typed_character_count >= self.prompt.get_prompt_character_count():
                # Stop the test
                self.test_end = timer()
                self.entry.disable()
                self.test_status = STATUS_FINISHED

                # Calculate and present results
                speed = self._calculate_wpm(self.test_start,
                                            self.test_end,
                                            self.prompt.get_prompt_word_count())
                accuracy = self._calculate_accuracy(self.prompt.get_prompt_content(),
                                                    self.entry.get_entry_content(),
                                                    typed_character_count)
                self.console.update_result(speed, accuracy)

        self.console.update_status(self.test_status)

    # Reset the display and update the test status to 'not started'
    def reset(self, event):
        self.entry.reset()
        self.console.update_result()
        self.test_status = STATUS_NOT_STARTED
        self.console.update_status(self.test_status)

    @staticmethod
    def _calculate_wpm(start_sec, end_sec, word_count):
        minutes = (end_sec - start_sec) / 60
        return int(word_count // minutes)

    @staticmethod
    def _calculate_accuracy(str1, str2, character_count):
        dl_distance = jellyfish.damerau_levenshtein_distance(str1, str2)
        success_ratio = 1 - (dl_distance / character_count)
        return int(success_ratio * 100)
