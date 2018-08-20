import curses
import time
from random import randint
from alien_space1 import *

al2 = []
c2 = 0


class Alien2:
    marker = "A"

    def __init__(self, old, win):
        self.a = al1.pop(al1.index(old))
        self.a[0] = len(al2)
        self.a[1] = time.time()
        self.a[2] = 2
        self.a[5] = self
        al2.append(self.a)
        win.addch(self.a[3], self.a[4], self.marker)

    def getalien(self):

        return self.a
