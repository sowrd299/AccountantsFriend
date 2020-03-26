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
        gui.update(am)

    window.bind("<Key>", on_key)

    def on_backspace(e):
        am.process_backspace()
        gui.update(am)

    window.bind("<BackSpace>", on_backspace)
    window.bind("<Right>", on_backspace)

    def on_return(e):
        am.process_char("=")
        gui.update(am)

    window.bind("<Return>", on_return)

    # go
    window.title("Adding Machine")
    window.mainloop()


if __name__ == '__main__':
    main()