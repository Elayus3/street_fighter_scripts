import pydirectinput as pag
import time
import keyboard
import cammy

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

start = False
while not start:
    if keyboard.is_pressed('e'): break

stop = False
while not stop:
    # make_hadouken('LP')
    # if keyboard.is_pressed('o'): hadouken('LP')
    # if keyboard.is_pressed('i'): shoryuken('LP')
    # if keyboard.is_pressed('u'): shinku_hadouken('LP')
    # if keyboard.is_pressed('o'): cammy.spiral_arrow(buttons['HK'], 'left')
    # if keyboard.is_pressed('p'): cammy.spiral_arrow(buttons['HK'], 'right')
    # if keyboard.is_pressed('u'): cammy.cannon_spike(buttons['HK'], 'left')
    # if keyboard.is_pressed('i'): cammy.cannon_spike(buttons['HK'], 'right')
    # if keyboard.is_pressed('y'): cammy.V_skill()

    if keyboard.is_pressed('r'): cammy.combo3('left')
    if keyboard.is_pressed('t'): cammy.combo3('right')

    if keyboard.is_pressed('q'):
        stop = True
    
# while True:                            
#     if keyboard.is_pressed('q'): break