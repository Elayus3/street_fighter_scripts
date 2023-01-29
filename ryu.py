import pydirectinput as pag

def hadouken(punch):
    pag.keyDown('s')
    pag.keyDown('d')
    pag.keyUp('s')
    pag.press(buttons[punch])
    pag.keyUp('d')

def shoryuken(punch):
    pag.keyDown('d')
    pag.keyUp('d')
    pag.keyDown('s')
    pag.keyDown('d')
    pag.press(buttons[punch])
    pag.keyUp('s')
    pag.keyUp('d')

def shinku_hadouken(punch):
    pag.PAUSE=0.02
    pag.keyDown('s')
    pag.keyDown('d')
    pag.keyUp('s')
    pag.keyUp('d')
    pag.keyDown('s')
    pag.keyDown('d')
    pag.keyUp('s')
    pag.keyDown(buttons[punch])
    pag.keyUp('d')
    pag.keyUp(buttons[punch])
