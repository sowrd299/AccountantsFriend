'''
A class to manage and represent the opperations of an adding machine
'''

class AddingMachine():

    def __init__(self):
        self.total = 0
        self.number = ""

    # GETTERS AND SETTERS

    def get_total(self):
        return self.total

    def get_total_str(self):
        return str(self.total)

    def get_number_str(self):
        return self.number

    def get_number(self):
        return float(self.number) if self.number else 0

    # ACTUAL OPPERATIONS

    def do_op(self, op):
        self.total = op(self.get_total(), self.get_number())
        self.number = ""

    # I/O

    def process_char(self, char):

        if char.isdigit():
            self.number += char

        elif len(char) == 1 and char in "+-*/":
            self.do_op(lambda a,b : eval("{0}{1}{2}".format(a,char,b)))