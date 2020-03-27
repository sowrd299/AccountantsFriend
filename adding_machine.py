'''
A class to manage and represent the opperations of an adding machine
'''
class AddingMachine():

    base = 10

    def __init__(self):
        self.totals = [0.0]
        self.cached_ops = None
        self.entering_number = False # stores if we are currently midway through entering a number

    # GETTERS AND SETTERS

    def get_subtotals(self):
        return self.totals[:-1]

    def get_total(self):
        return self.totals[-2 if entering_number else -1]
        return str(self.get_total())

    def get_number(self):
        return self.totals[-1]

    def clear_number(self):
        self.entering_number = False

    # ACTUAL OPPERATIONS

    def do_op(self, op):
        if len(self.totals) >= 2:
            self.totals.append( op(self.totals.pop(-2), self.totals.pop(-1)) )
            self.clear_number()

    def do_cached_op(self):
        if len(self.totals) >= 1:
            self.totals.append( self.cached_op(self.totals.pop(-1)))

    def cache_op(self, op):
        self.cached_op = op

    def add_digit(self, val):

        if self.entering_number:
            self.totals[-1] *= self.base
            self.totals[-1] += val
        else:
            self.totals.append(val)

    # I/O

    def process_char(self, char):

        entered_number = False # tracks if we are in the middle of entering a number

        # typing a digit
        if char.isdigit():
            self.add_digit(float(char))
            entered_number = True

        # basic operations 
        elif len(char) == 1 and char in "+-":
            self.do_op(lambda a,b : eval("{0}{1}{2}".format(a,char,b)))

        # "cashed" operations
        elif len(char) == 1 and char in "/*":
            self.cache_op(lambda b : eval("{0}{1}{2}".format(self.totals.pop(-1),char,b)))
            self.totals.append(0.0) # starts a "new" stack layer for the new number

        elif char == "=":
            if self.entering_number:
                self.process_char("+") # assume preceding number was positive

            self.do_cached_op()

        # control operations
        #   all clear
        elif char == "C":
            self.__init__()

        # clearnup
        self.entering_number = entered_number


    def process_backspace(self):

        self.totals[-1] //= self.base
        self.entering_number = True
