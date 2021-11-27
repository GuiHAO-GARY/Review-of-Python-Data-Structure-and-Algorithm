# Create novel class to solve various problems
class Fraction:

    def __init__(self, top, bottom):
        # Create a fraction instance
        if top == int(top) and bottom == int(bottom):
            if bottom < 0:
                top = -top
                bottom = -bottom
            self.num = top  # numerator
            self.den = bottom  # denominator
        else:
            raise RuntimeError('Numerator and denominator should be integers')

    def show(self):
        # Show fraction in normal way
        print(self.num, '/', self.den)

    def __repr__(self):
        # When type Fraction(1, 3) will show 1/3
        return str(self.num) + '/' + str(self.den)

    def __str__(self):
        # Overwrite the __str__ method
        # When invoking print method
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        # Rewrite __add__ method
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)  # To generate irreducible fraction
        return Fraction(new_num // common, new_den // common)

    @staticmethod
    def gcd(m, n):
        """
        Find greatest common divisor of m and n
        Euclidean Algorithm
        """
        while m % n != 0:
            m, n = n, m % n
        return n

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num


# Inheritance: Logistic Gate and Circuit
class LogicGate:
    def __init__(self, name):
        self.label = name
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()  # Although not defined yet, it can be created here in advance
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        # There are 2 pins A and B as input
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            # Initial state (no connection), Input 0 or 1
            return int(input('Enter PinA input for gate' + self.getLabel() + '-->'))
        else:
            # This flow means pinA is connected to another gate
            # self.pinA is a Connector instance now
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            # Input 0 or 1
            return int(input('Enter PinB input for gate' + self.getLabel() + '-->'))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """
        When using connector, the current pin should be not empty
        :param source: Last logistic gate
        :return: None
        """
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError('Error: No Empty Pins')


class UnaryGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            # Input 0 or 1
            return int(input('Enter Pin input for gate' + self.getLabel() + '-->'))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error: No Empty Pins')


class AndGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, name):
        super().__init__(name)

    def performGateLogic(self):
        a = self.getPin()
        if a == 0:
            return 1
        else:
            return 0


class Connector:
    """
    Connect gate instances
    """
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.setNextPin(self)  # to check whether to_gate has vacant pin

    def getFrom(self):
        return self.from_gate

    def getTo(self):
        return self.to_gate


if __name__ == '__main__':
    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)
    print('Construct f1 = Fraction(1, 4) -> {}'.format(f1))
    print('Construct f2 = Fraction(1, 4) -> {}'.format(f2))
    f3 = f1 + f2
    print('f1 + f2 = {}'.format(f3))
    print('Compare f1 and f2 -> Equal: {}'.format(f1 == f2))
    print('Compare f1 and Fraction(2, 8) -> Equal: {}'.format(f1 == Fraction(2, 8)))

    print('**************************************\n')

    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)

    result = g4.getOutput()
    print('Final output is {}'.format(result))



