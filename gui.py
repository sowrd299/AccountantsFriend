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

        self.top_frame = tkinter.Frame(self)
        self.top_frame.pack(fill = tkinter.X)

        # DISPLAY CURRENT SUBTOTALS
        self.subtotals_v = tkinter.StringVar()
        self.subtotals = tkinter.Label(self.top_frame, textvariable=self.subtotals_v, bg=self.bg2, fg=self.fg, font=(self.font, 12), anchor=tkinter.W)
        self.subtotals.pack(fill = tkinter.X)

        # THE MAIN NUMERIC DISPLAY
        self.number_v = tkinter.StringVar()
        self.number = tkinter.Label(self, textvariable=self.number_v, width=18, bg=self.bg, fg=self.fg, font=(self.font, 24), anchor=tkinter.E)
        self.number.pack()

    def get_number_disp(self, am):
        return str(am.get_number())

    def update(self, am):
        self.subtotals_v.set("Subtotals: " + " ".join(map(lambda x : str(x) + " +", am.get_subtotals())))
        self.number_v.set(self.get_number_disp(am))

