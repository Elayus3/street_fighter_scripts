import pydirectinput as pag
import time
import keyboard

buttons = {
    'LP': 'g',
    'MP': 'h',
    'HP': 'j',
    'LK': 'b',
    'MK': 'n',
    'HK': 'm',
    '2': 's',
    '3': 'sd',
    '6': 'd',
    '9': 'wd',
    '8': 'w',
    '7': 'aw',
    '4': 'a',
    '1': 'as',
}

# def type_(*orders):
#     chars = [buttons[order] for order in orders] 
#     for char in chars:
#         if len(char) == 1: pag.press(char); time.sleep(.001)
#         else: 
#             for char in chars: pag.keyDown(char); time.sleep(.001)
#             for char in chars: pag.keyUp(char); time.sleep(.001)

# def make_hadouken(punch): type_('2', '3', '6', punch)

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


start = False
while not start:
    if keyboard.is_pressed('e'): break

stop = False
while not stop:
    # make_hadouken('LP')
    if keyboard.is_pressed('o'): hadouken('LP')
    if keyboard.is_pressed('i'): shoryuken('LP')
    if keyboard.is_pressed('u'): shinku_hadouken('LP')


    if keyboard.is_pressed('q'):
        stop = True
    
# while True:                            
#     if keyboard.is_pressed('q'): break