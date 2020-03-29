from adding_machine import AddingMachine, CharOp

'''
A class to represent an entry on the tape
'''
class TapeEntry():

    fstr = "{0} {1}\n"

    def __init__(self, number, op):
        self.number = number
        self.op = op

    def __str__(self):
        return self.fstr.format(self.number, self.op)

class TextTapeEntry(TapeEntry):
    
    def __init__(self, text):
        self.fstr = "{0}\n".format(text)
        super().__init__(0, CharOp("+"))

BLANK_TAPE_ENTRY = TextTapeEntry("")


'''
A class to represent the tape output of an adding machine
'''
class AddingMachineTape():

    def __init__(self):
        self.entries = []

    def append(self, *args, **kwargs):
        self.entries.append(TapeEntry(*args, **kwargs))

    def new_line(self):
        self.entries.append(BLANK_TAPE_ENTRY)

    def __str__(self):
        r = "".join(map(str, self.entries))
        if len(r) > 0 and r[-1] == "\n":
            r = r[:-1]
        return r


'''
An adding machine that records all its operations to a tape
'''
class TapedAddingMachine(AddingMachine):

    def __init__(self):
        super().__init__()
        self.tape = AddingMachineTape()

    def get_tape(self):
        return self.tape

    def do_op(self, op):
        self.tape.append(self.get_number(), op)
        return super().do_op(op)

    def cache_op(self, op):
        self.tape.new_line()
        self.tape.append(op.a, op)
        return super().cache_op(op)

    def do_cached_op(self):
        self.tape.new_line()
        return super().do_cached_op()
    