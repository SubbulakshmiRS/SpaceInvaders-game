import curses
miss1 = []
miss2 = []


class Missile:

    def __init__(self, x):
        self.m = {0: len(miss1), 1: 1, 2: 2, 3: x, 4: self}


class Missile1(Missile):

    marker = "I"

    def __init__(self, x, win):
        Missile.__init__(self, x)
        miss1.append(self.m)
        win.addch(self.m[2], self.m[3], self.marker)


class Missile2(Missile):

    marker = "i"

    def __init__(self, x, win):
        Missile.__init__(self, x)
        miss2.append(self.m)
        win.addch(self.m[2], self.m[3], self.marker)
