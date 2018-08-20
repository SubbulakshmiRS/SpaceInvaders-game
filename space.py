import curses
from random import randint
ship = []


class Spaceship:

    marker = "$"

    def __init__(self, win):

        self.s = {0: len(ship), 1: 1, 2: 1, 3: randint(1, 8), 4: self}
        win.addch(self.s[2], self.s[3], self.marker)
        ship.append(self.s)

    def move_right(self, win):

        i = self.s[0]
        s = ship[i]
        win.addch(self.s[2], self.s[3], " ")
        s[3] = s[3] if s[3] > 7 else s[3]+1
        win.addch(self.s[2], self.s[3], self.marker)

    def move_left(self, win):

        i = self.s[0]
        s = ship[i]
        win.addch(self.s[2], self.s[3], " ")
        s[3] = s[3] if s[3] < 2 else s[3]-1
        win.addch(self.s[2], self.s[3], self.marker)
