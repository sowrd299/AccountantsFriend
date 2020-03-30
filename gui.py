import tkinter

class TapeTextArea(tkinter.Frame):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.kwargs = kwargs
        self.create_widgets()
        self.rows = kwargs["height"]

    def create_widgets(self):

        # GRID
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # TEXT AREA
        self.text = tkinter.Text(self, **self.kwargs, width=-1, relief = tkinter.FLAT)
        self.text.grid(row = 0, column = 0, sticky="nsew")
        self.create_text_format()

        # SCROLL
        self.scroll_area = self.text # pseudonim for whatever widget will be scrolled through
        self.scrollbar = tkinter.Scrollbar(self, command=self.scroll_area.yview)
        self.scrollbar.grid(row=0, column=1, sticky='nsew')
        self.scroll_area.config(yscrollcommand =  self.scrollbar.set)

    def create_text_format(self):
        self.text.tag_configure("body", justify="right")

    def format_text(self):
        self.text.tag_add("body", "1.0", tkinter.END)

    def update(self, tape):
        # set the text
        self.text.delete("1.0", tkinter.END)
        self.text.insert(tkinter.END, ("\n" * (self.rows-1)) + str(tape))
        # display it correctly
        self.format_text()
        self.text.see(tkinter.END)


'''
A class to dispay the resault of the adding machine to the user
'''
class GUI(tkinter.Frame):

    bg = "#111111"
    fg = "#c0f0ee" 

    bg2 = "#050505"

    light_bg = "#c0c0d0"
    light_fg = bg2

    font = "Helvetica"

    def __init__(self, parent):
        super().__init__(parent)
        parent.resizable(False, False)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # THE TAPE
        self.tape = TapeTextArea(self, bg = self.light_bg, fg = self.light_fg, font=(self.font, 14), height=8)
        self.tape.pack(fill = tkinter.BOTH)

        # THE BAR OF OPTIONS
        self.top_frame = tkinter.Frame(self, bg=self.bg2)
        self.top_frame.pack(fill = tkinter.X)

        # OPEN HELP MENU
        self.help_button = tkinter.Button(self.top_frame, text="Help", command = self.open_help, bg=self.bg2, fg=self.fg, font=(self.font, 8), relief=tkinter.FLAT)
        self.help_button.pack(side = tkinter.LEFT)

        # DISPLAY CURRENT SUBTOTALS
        self.subtotals_v = tkinter.StringVar()
        self.subtotals = tkinter.Label(self.top_frame, textvariable=self.subtotals_v, bg=self.bg2, fg=self.fg, font=(self.font, 12), anchor=tkinter.W)
        self.subtotals.pack(side = tkinter.LEFT)#fill = tkinter.X)

        # THE MAIN NUMERIC DISPLAY
        self.number_v = tkinter.StringVar()
        self.number = tkinter.Label(self, textvariable=self.number_v, width=18, bg=self.bg, fg=self.fg, font=(self.font, 24), anchor=tkinter.E)
        self.number.pack()

    def get_number_disp(self, am):
        return str(am.get_number())

    def update(self, am):
        self.tape.update(am.get_tape())
        self.subtotals_v.set(" Running Subtotals: " + ", ".join(map(lambda x : str(x) , am.get_subtotals())))
        self.number_v.set(self.get_number_disp(am))

    def open_help(self):
        window = tkinter.Toplevel(self)
        help_gui = HelpGUI(window)


'''
A GUI for displaying the command available
'''
class HelpGUI(GUI):

    help_text = [
        'KEYBOARD COMMANDS:',
        'x/c: Copy number to clipboard.',
        't: Copy the tape to clipboard.',
        'v: Paste number from clipboard.',
        'C: Clear All/Complete reset.',
        'Backspace/Right Arrow:\n\tDelete least significant digit.',
        '+, -, *, /, =, and number keys:\n\tWork like an adding machine.',
        'Enter: Same as "="; numpad enter may not work.',
        '\n©2020 Ryan N. Ward' 
    ]
    

    def create_widgets(self):

        self.labels = []
        for i,line in enumerate(self.help_text):

            bg = self.bg if i % 2 else self.bg2
            formated_line = "{0}:\t{1}".format(*line.split(":")) if ":" in line else line
            font = (self.font, 12) + (("bold",) if i == 0 else tuple())

            label = tkinter.Label(self, text=formated_line, bg=bg, fg=self.fg, font=font, anchor=tkinter.W, justify=tkinter.LEFT)
            label.pack(fill = tkinter.X)
            self.labels.append(label)

    def update(self):
        pass
