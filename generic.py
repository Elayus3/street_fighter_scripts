import pydirectinput as pag

def QC(key1, direction):
    pag.PAUSE=0.02
    assert direction in ['right', 'left']
    key_direction = 'd' if direction=='right' else 'a'
    pag.keyDown('s')
    pag.keyDown(key_direction)
    pag.keyUp('s')
    pag.press(key1)
    pag.keyUp(key_direction)

def Z_move(key1, direction):
    pag.PAUSE=0.02
    assert direction in ['right', 'left']
    key_direction = 'd' if direction=='right' else 'a'
    pag.keyDown(key_direction)
    pag.keyUp(key_direction)
    pag.keyDown('s')
    pag.keyDown(key_direction)
    pag.press(key1)
    pag.keyUp('s')
    pag.keyUp(key_direction)

def V_skill():
    pag.PAUSE=0.001
    pag.keyDown('n')
    pag.keyDown('h')
    pag.keyUp('n')
    pag.keyUp('h')