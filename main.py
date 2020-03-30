import tkinter

from taped_adding_machine import TapedAddingMachine
from gui import GUI

def main():
    
    # CREATE THE MAIN OBJECTS
    am = TapedAddingMachine()
    window = tkinter.Tk()
    gui = GUI(window)

    # EVENT BINDINGS
    def on_key(e): 
        am.process_char(e.char)

        # UI and I/O, and top-level command keys
        # Copy
        if e.char in 'xc':
            window.clipboard_clear()
            window.clipboard_append(str(am.get_number()))
        # Copy tape
        elif e.char in 't':
            window.clipboard_clear()
            window.clipboard_append(str(am.get_tape()))
        # Paste
        elif e.char in 'v':
            am.process_char(window.clipboard_get())
        # All clear
        elif e.char in 'C':
            am.__init__()

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

    am.set_decimals(gui.decimal_v)
    am.set_decimals(2) # default number of decimals

    # GO
    gui.update(am)
    window.title("Adding Machine")
    window.mainloop()


if __name__ == '__main__':
    main()