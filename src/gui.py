"""
The file to hold the Alkalinity Titrator's GUI class
"""

# pylint: disable = too-many-locals, too-many-statements

import threading
import time
import tkinter as tk

STICKY = tk.E + tk.W + tk.S + tk.N
FONT = ("Courier", 15)
TEXTBOX_WIDTH = 15
LABEL_WIDTH = 20
BUTTON_WIDTH = 8
WIDTH = 22
FG = "white"
BG = "blue"
ANCHOR = "w"


class GUI:
    """
    The class for the Alkalinity Titrator's GUI
    """

    def __init__(self, titrator):
        """
        The GUI for the Alkalinity Titrator
        """

        # Keep an Instance of the Titrator
        self.titrator = titrator

        # Initialize the GUI Frame
        self.root = tk.Tk()
        self.root.geometry("560x200")
        self.root.title("Tank Controller")
        self.root.configure(background="black")

        # Split window into left and right sections
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # ---------------------------------------------------------
        # LEFT SIDE - LCD AND KEYPAD
        # ---------------------------------------------------------

        left_frame = tk.Frame(self.root, bg="lightgray")
        left_frame.grid(row=0, column=0, sticky=STICKY)

        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)

        # Initialize the Labels
        label_frame = tk.Frame(left_frame)
        label_frame.config(bg=BG)

        label_frame.columnconfigure(0, weight=1)
        label_frame.rowconfigure(0, weight=1)
        label_frame.rowconfigure(1, weight=1)
        label_frame.rowconfigure(2, weight=1)
        label_frame.rowconfigure(3, weight=1)

        self.line_1 = tk.Label(
            label_frame,
            text=self.titrator.lcd.get_line(1),
            fg=FG,
            bg=BG,
            font=FONT,
            width=WIDTH,
            anchor=ANCHOR,
        )
        self.line_1.grid(row=0, column=0, sticky=STICKY)

        self.line_2 = tk.Label(
            label_frame,
            text=self.titrator.lcd.get_line(2),
            fg=FG,
            bg=BG,
            font=FONT,
            width=WIDTH,
            anchor=ANCHOR,
        )
        self.line_2.grid(row=1, column=0, sticky=STICKY)

        self.line_3 = tk.Label(
            label_frame,
            text=self.titrator.lcd.get_line(3),
            fg=FG,
            bg=BG,
            font=FONT,
            width=WIDTH,
            anchor=ANCHOR,
        )
        self.line_3.grid(row=2, column=0, sticky=STICKY)

        self.line_4 = tk.Label(
            label_frame,
            text=self.titrator.lcd.get_line(4),
            fg=FG,
            bg=BG,
            font=FONT,
            width=WIDTH,
            anchor=ANCHOR,
        )
        self.line_4.grid(row=3, column=0, sticky=STICKY)

        label_frame.grid(row=0, column=0, sticky=STICKY)

        # Initialize the Buttons
        buttonframe = tk.Frame(left_frame)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)

        tk.Button(
            buttonframe,
            text="1",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("1"),
        ).grid(row=4, column=0, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="2",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("2"),
        ).grid(row=4, column=1, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="3",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("3"),
        ).grid(row=4, column=2, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="A",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("A"),
        ).grid(row=4, column=3, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="4",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("4"),
        ).grid(row=5, column=0, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="5",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("5"),
        ).grid(row=5, column=1, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="6",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("6"),
        ).grid(row=5, column=2, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="B",
            width=8,
            command=lambda: self.button_press("B"),
        ).grid(row=5, column=3, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="7",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("7"),
        ).grid(row=6, column=0, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="8",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("8"),
        ).grid(row=6, column=1, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="9",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("9"),
        ).grid(row=6, column=2, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="C",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("C"),
        ).grid(row=6, column=3, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="*",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("*"),
        ).grid(row=7, column=0, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="0",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("0"),
        ).grid(row=7, column=1, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="#",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("#"),
        ).grid(row=7, column=2, sticky=STICKY)

        tk.Button(
            buttonframe,
            text="D",
            width=BUTTON_WIDTH,
            command=lambda: self.button_press("D"),
        ).grid(row=7, column=3, sticky=STICKY)

        buttonframe.grid(row=1, column=0, sticky=STICKY)

        # ---------------------------------------------------------
        # RIGHT SIDE - BOARD LED
        # ---------------------------------------------------------

        right_frame = tk.Frame(self.root, bg="darkgray")
        right_frame.grid(row=0, column=1, sticky=STICKY)

        right_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(1, weight=1)
        right_frame.rowconfigure(0, weight=1)

        self.led_canvas = tk.Canvas(
            right_frame,
            width=80,
            height=80,
            bg="darkgray",
            highlightthickness=0,
        )
        self.led_canvas.grid(row=0, column=0, padx=30, sticky=tk.E)

        self.led_circle = self.led_canvas.create_oval(
            5,
            5,
            50,
            50,
            fill="red",
            outline="black",
            width=3,
        )

        self.led_label = tk.Label(
            right_frame,
            text="Board LED",
            font=("Arial",12),
            bg="darkgray",
            fg="black",
        )
        self.led_label.grid(row=0, column=1, padx=20, sticky=tk.W)

        # Start GUI update thread
        self.thread = threading.Thread(
            target=self.update_gui,
            daemon=True,
        )
        self.thread.start()

        self.root.mainloop()

    def button_press(self, key):
        """
        The function to facilitate button presses
        """
        self.titrator.keypad.set_key(key)

    def update_gui(self):
        """
        The function to update the GUI LCD and LED
        """
        while True:
            time.sleep(0.001)

            self.line_1.config(
                text=self.titrator.lcd.get_line(1),
                anchor=self.titrator.lcd.get_style(1),
            )
            self.line_2.config(
                text=self.titrator.lcd.get_line(2),
                anchor=self.titrator.lcd.get_style(2),
            )
            self.line_3.config(
                text=self.titrator.lcd.get_line(3),
                anchor=self.titrator.lcd.get_style(3),
            )
            self.line_4.config(
                text=self.titrator.lcd.get_line(4),
                anchor=self.titrator.lcd.get_style(4),
            )

            if self.titrator.led.is_on:
                self.led_canvas.itemconfig(
                    self.led_circle,
                    fill="yellow",
                )
            else:
                self.led_canvas.itemconfig(
                    self.led_circle,
                    fill="black",
                )
