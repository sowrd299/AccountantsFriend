import tkinter

from taped_adding_machine import TapedAddingMachine
from gui import GUI

def main():
    
    # CREATE THE MAIN OBJECTS
    am = TapedAddingMachine()
    window = tkinter.Tk()
    gui = GUI(window)
    gui.update(am)

    # EVENT BINDINGS
    def on_key(e): 
        am.process_char(e.char)

        # UI and I/O, and top-level command keys
        # Copy
        if e.char in 'xc':
            window.clipboard_clear()
            window.clipboard_append(str(am.get_number()))
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

    # GO
    window.title("Adding Machine")
    window.mainloop()


if __name__ == '__main__':
    main()