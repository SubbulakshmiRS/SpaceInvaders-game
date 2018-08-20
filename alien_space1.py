import curses
import time
from random import randint


al1 = []
c1 = 0


class Alien:

    marker = "a"

    def __init__(self, win):

        self.a = {0: len(al1), 1: time.time(), 2: 1,
                  3: randint(7, 8), 4: randint(1, 8), 5: self}
        win.addch(self.a[3], self.a[4], self.marker)
        al1.append(self.a)

    def getalien(self):

        return self.a
