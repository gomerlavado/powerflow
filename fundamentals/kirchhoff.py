
class Node:
    """ 
    Super class for nodes.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def getname(self):
        return self.name


class Edge():
    """
    first and second are ids from nodes.
    """
    def __init__(self, id, first, second, name):
        self.id = id
        self.first = first
        self.second = second
        self.name = name


class Generator(Node):
    def __init__(self, id, name, power):
        super().__init__(id, name)
        self.power = power


class Load(Node):
    def __init__(self, id, name, power):
        super().__init__(id, name)
        self.power = power


class Line(Edge):
    def __init__(self, id, first, second, name, power = None):
        super().__init__(id, first, second, name)
        self.power = power

    def conj(self):
        return complex(- self.power.real, self.power.imag)


class Bus(Node):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.net = complex(0,0)
    
    def addgen(self, node):
        self.net += node.power

    def addload(self, node):
        self.net -= node.power
        
    def addline(self, line):
        if line.first == self.id:
            self.net -= line.power
        elif line.second == self.id:
            self.net -= line.conj()
        else:
            raise ValueError("Line ends are not defined")
            
    def getnet(self):
        return complex(round(self.net.real,3), round(self.net.imag,3))
    

generator1 = Generator(1, "G1", 1 + 1j)
load1 = Load(1, "D1", 1 - 1j)
line1 = Line(1, 1, 2, "L1", 0.5 + 0.2j)

bus1 = Bus(1, "B1")
bus1.addgen(generator1)
bus1.addload(load1)
bus1.addline(line1)

generator2 = Generator(2, "G2", 0.5 + 0.5j)
load2 = Load(2, "D2", 1 + 1j)

bus2 = Bus(2, "B2")
bus2.addgen(generator2)
bus2.addload(load2)
bus2.addline(line1)

capacitance1 = Generator(4, "C1", 1j)
line2 = Line(2, 1, 3, "L2")
line2.power = bus1.getnet()

line3 = Line(3, 2, 3, "L3")
line3.power = bus2.getnet()

bus3 = Bus(3, "B3")
bus3.addgen(capacitance1)
bus3.addline(line2)
bus3.addline(line3)

print(bus1.getnet())
print(bus2.getnet())
print(bus3.getnet())
