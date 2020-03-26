import tkinter

from adding_maching import AddingMachine
from gui import GUI

def main():
    
    # create the main objects
    am = AddingMachine()
    window = tkinter.Tk()
    gui = GUI(window)
    gui.update(am)

    # event binging
    def on_key(e): 
        am.process_char(e.char)
        print(am.get_number_str())
        gui.update(am)

    window.bind("<Key>", on_key)

    # go
    window.mainloop()


if __name__ == '__main__':
    main()