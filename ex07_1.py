def get(value):
    try:
        val = int(value)
    except ValueError:
        val = circuit[value].value()

    return val


class ConstantGate:
    def __init__(self, a):
        self.a = a
        self.val = None

    def value(self):
        if self.val == None:
            self.val = get(self.a)

        return self.val

class NotGate:
    def __init__(self, a):
        self.a = a
        self.val = None

    def value(self):
        if self.val == None:
            self.val = 65535 - get(self.a)

        return self.val

class AndGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = None

    def value(self):
        if self.val == None:
            self.val = get(self.a) & get(self.b)

        return self.val

class OrGate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = None

    def value(self):
        if self.val == None:
            self.val = get(self.a) | get(self.b)

        return self.val

class LShiftGate:
    def __init__(self, a, amt):
        self.a = a;
        self.amt = int(amt);
        self.val = None

    def value(self):
        if self.val == None:
            self.val = get(self.a) << self.amt

        return self.val

class RShiftGate:
    def __init__(self, a, amt):
        self.a = a;
        self.amt = int(amt);
        self.val = None

    def value(self):
        if self.val == None:
            self.val = get(self.a) >> self.amt

        return self.val

circuit = {}

classes = {
    "CONST": ConstantGate,
    "AND": AndGate,
    "OR": OrGate,
    "LSHIFT": LShiftGate,
    "RSHIFT": RShiftGate,
    "NOT": NotGate
}

def parse(line):
    parts = line.strip().split(" -> ")
    wire = parts.pop()
    args = parts[0].split(' ')

    if len(args) == 1:
        args = ['CONST'] + args

    if len(args) == 3:
        cmd = args.pop(1)
        args = [cmd] + args

    return [wire] + args

def connect(wire, cmd, *args):
    Gate = classes[cmd]
    circuit[wire] = Gate(*args)

with open("ex07-input.txt") as file:
    for line in file:
       connect(*parse(line))

    # this is all that is needed for part 2
    # circuit["b"].val = 16076

    # for wire, gate in circuit.iteritems():
    #     print wire + ' ' + str(gate.value())

    print circuit["a"].value()
