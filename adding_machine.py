def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

'''
A class that represents a operation represented by a string
    e.g., and math operator with an assigned character
'''
class CharOp():

    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

    def __call__(self, a, b):
        return eval( "{0}{1}{2}".format(a, self.char, b) )

'''
A subclass that stores the left operand
'''
class PartialCompleteCharOp(CharOp):

    def __init__(self, a, char):
        super().__init__(char)
        self.a = a

    def __call__(self, b):
        return super().__call__(self.a, b)


'''
A class to manage and represent the opperations of an adding machine
'''
class AddingMachine():

    # THE BASE ALL NUMBERS ARE ENTERED IN
    base = 10

    # THE NUMBER OF DECIMALS ALL NUMBERS ARE ENTERED WITH
    decimals = 0

    def __init__(self):
        self.totals = [0.0]
        self.cached_ops = [lambda x : x]
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

    def set_decimals(self, val):
        self.decimals = val

    def round_number(self):
        self.totals[-1] = round(self.totals[-1], self.decimals)

    # ACTUAL OPPERATIONS

    def do_op(self, op):
        if len(self.totals) >= 2:
            self.totals.append( op(self.totals.pop(-2), self.totals.pop(-1)) )
            self.clear_number()
        self.round_number()

    def do_cached_op(self):
        if len(self.totals) >= 1 and len(self.cached_ops) >= 1:
            self.totals.append( self.cached_ops.pop(-1)(self.totals.pop(-1)) )
        self.round_number()

    def cache_op(self, op):
        self.cached_ops.append(op)

    def add_digit(self, val):

        val /= (self.base ** self.decimals) # apply the apropriate number of decimals

        if self.entering_number:
            self.totals[-1] *= self.base
            self.totals[-1] += val
        else:
            self.totals.append(val)

        self.round_number()

    # I/O

    def process_char(self, char):

        entered_number = False # tracks if we are in the middle of entering a number

        # typing a digit
        if isfloat(char):
            self.add_digit(float(char))
            entered_number = True

        # basic operations 
        elif len(char) == 1 and char in "+-":
            self.do_op(CharOp(char))

        # "cashed" operations
        elif len(char) == 1 and char in "/*":
            self.cache_op(PartialCompleteCharOp(self.totals.pop(-1), char))
            self.totals.append(0.0) # starts a new stack "layer" for the new number

        elif char == "=":
            if self.entering_number:
                self.process_char("+") # assume preceding number was positive

            self.do_cached_op()

        # clearnup
        self.entering_number = entered_number


    def process_backspace(self):

        self.totals[-1] /= self.base
        self.round_number()
        self.entering_number = True
