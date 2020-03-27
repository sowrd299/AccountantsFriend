import tkinter

'''
A class to dispay the resault of the adding machine to the user
'''

class GUI(tkinter.Frame):

    bg = "#111111"
    bg2 = "#050505"
    fg = "#c0f0ee" 

    font = "Helvetica"

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.top_frame = tkinter.Frame(self, bg=self.bg2)
        self.top_frame.pack(fill = tkinter.X)

        # OPEN HELP MENU
        self.help_button = tkinter.Button(self.top_frame, text="Help", command = self.open_help, bg=self.bg2, fg=self.fg, font=(self.font, 8))
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
        self.subtotals_v.set(" Subtotals: " + ", ".join(map(lambda x : str(x) , am.get_subtotals())))
        self.number_v.set(self.get_number_disp(am))

    def open_help(self):
        window = tkinter.Toplevel(self)
        help_gui = HelpGUI(window)


'''
A GUI for displaying the command available
'''
class HelpGUI(GUI):

    help_text = "\n".join([
        'COMMANDS:',
        '"x"/"c": Copy number to clipboard',
        '"v": Paste number from clipboard',
        '"C": Clear All/Complete reset',
        'Backspace/Right Arrow: Delete least significant digit',
        '"+", "-", "*", "/", "=", and number keys:',
        '\tWork like an adding machine',
        'Enter: Same as "="; numpad enter may not work'
    ])
    

    def create_widgets(self):

        self.help_label = tkinter.Label(self, text=self.help_text, bg=self.bg, fg=self.fg, font=(self.font, 12), justify=tkinter.LEFT)
        self.help_label.pack()

    def update(self):
        pass
