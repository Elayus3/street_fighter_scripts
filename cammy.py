## V-skill I, V-trigger II
import time

from generic import *

def spiral_arrow(kick, direction): QC(kick, direction)
def cannon_spike(kick, direction): Z_move(kick, direction)

def combo3(direction):
    pag.PAUSE=0.02
    key_direction = 'd' if direction=='right' else 'a'
    pag.keyDown(key_direction); time.sleep(.05)
    pag.keyUp(key_direction); time.sleep(.2)
    pag.keyDown(key_direction)
    pag.keyDown('w')
    pag.keyUp(key_direction)
    pag.keyUp('w')
    time.sleep(.45)
    pag.press('j'); time.sleep(.4)
    pag.press('h'); time.sleep(.3)
    pag.keyDown('s')
    pag.keyDown('n')
    pag.keyUp('s')
    pag.keyUp('n')
    QC('m', direction)