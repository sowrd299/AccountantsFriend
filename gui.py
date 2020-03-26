import tkinter

'''
A class to dispay the resault of the adding machine to the user
'''

class GUI(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.number_v = tkinter.StringVar()
        self.number = tkinter.Label(self, textvariable=self.number_v, width=18, bg="#111111", fg="#c0f0ee", font=("Helvetica", 24), anchor=tkinter.E)
        self.number.pack()

    def get_number_disp(self, am):
        number = am.get_number_str()
        if not number:
            return am.get_total_str()
        else:
            return number

    def update(self, am):
        self.number_v.set(self.get_number_disp(am))

