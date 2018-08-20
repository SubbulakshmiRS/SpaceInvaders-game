
import os
import threading
import sys

from space import *
from alien_space1 import *
from alien_space2 import *
from missile_1_2 import *

curses.initscr()
win = curses.newwin(10, 10, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

count = 0


def move_miss():

    for m in miss2:
        win.addch(m[2], m[3], " ")
        if m[2] < 7:
            m[2] = m[2]+2
            win.addch(m[2], m[3], m[4].marker)
        else:
            m = miss2.pop(miss2.index(m))

    for m in miss1:
        win.addch(m[2], m[3], " ")
        if m[2] < 8:
            m[2] = m[2]+1
            win.addch(m[2], m[3], m[4].marker)
        else:
            m = miss1.pop(miss1.index(m))

    threading.Timer(1, move_miss).start()


class Engine:

    def __init__(self):

        pass

    def die(self):

        for a in al1:
            if time.time() - a[1] >= 8:
                a = al1.pop(al1.index(a))
                win.addch(a[3], a[4], " ")

        for a in al2:
            if time.time() - a[1] >= 5:
                a = al2.pop(al2.index(a))
                win.addch(a[3], a[4], " ")
        threading.Timer(1, self.die).start()

    def spawn(self):
        c = Alien(win)
        threading.Timer(10, self.spawn).start()

    def run(self):
        self.die()


e = Engine()
e.spawn()
e.run()
s = Spaceship(win)
move_miss()
run = 1
while run:
    for a in al1:
        for m in miss1:
            if m[2] == a[3] and m[3] == a[4]:
                #global count
                count = count + 1
                win.addch(m[2], m[3], " ")
                a1 = Alien2(a, win)
                m = miss1.pop(miss1.index(m))

        for m in miss2:
            if (m[2] == a[3] and m[3] == a[4]) or (m[2] == a[3]-1 and m[3] == a[4]):
                #global count
                count = count+1
                win.addch(m[2], m[3], " ")
                m = miss2.pop(miss2.index(m))

    event = win.getch()
    #print("SCORE ",count)
    if event == ord('q'):
        curses.endwin()
        #run = 0
        break
    elif event == ord('a'):
        s.move_left(win)
    elif event == ord('d'):
        s.move_right(win)
    elif event == ord('s'):
        m2 = Missile2(ship[0][3], win)
    elif event == ord(' '):
        m2 = Missile1(ship[0][3], win)
    else:
        pass

#sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
#global count
print("THE SCORE : ", count)
sys.exit(0)
