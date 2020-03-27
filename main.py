import tkinter

from adding_machine import AddingMachine
from gui import GUI

def main():
    
    # CREATE THE MAIN OBJECTS
    am = AddingMachine()
    window = tkinter.Tk()
    gui = GUI(window)
    gui.update(am)

    # EVENT BINDINGS
    def on_key(e): 
        am.process_char(e.char)

        # UI and I/O command keys
        if e.char in 'xc':
            window.clipboard_clear()
            window.clipboard_append(str(am.get_number()))
        elif e.char in 'v':
            am.process_char(window.clipboard_get())

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

    # GO
    window.title("Adding Machine")
    window.mainloop()


if __name__ == '__main__':
    main()