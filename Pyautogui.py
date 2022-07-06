from pyautogui import screenshot, press, write, hotkey, moveRel
from random import random
from time import sleep


def Shot(loc = f"C:\\Users\\abc\Pictures\Screenshots\\{random()}.png"):
    screenshot(loc)
    return loc

def Start(txt):
    press('win')  
    sleep(0.1)
    write(txt)
    sleep(0.1)
    press('enter')



# Whatsapp automation
def WhatMessage(reciver,message):
    Start('whatsapp')
    sleep(5)
    write(reciver)
    sleep(2)
    press('num2')
    sleep(2)
    press('enter')
    sleep(22)
    write(message)
    sleep(5)
    press('enter')

# Download automation
def Download(txt):
    Start('store')
    sleep(10)
    hotkey('ctrl','f')
    sleep(2)
    write(txt.replace('download',''))
    press('enter')
Download('download oneDrive')

    


#sleep(3)

#print(pyautogui.size())
#print(pyautogui.position())

# Move the mouse over 0 seconds
#pyautogui.moveTo(500,50
# hi
# 0)


# Move the mouse relative to its curent position in 3 sec
#pyautogui.moveRel(-100,100,3)

# To use Mouse click
#pyautogui.click(300,300,1,3,button="right") # ( x, y, no of clicks, time)
#pyautogui.leftClick()

#pyautogui.tripleClick()

# Scroll
#pyautogui.scroll(300)

# Mouse Up and down 
#mouseDown(100,100,button='left')

# Drag
#pyautogui.dragRel(100,100)

# Keyboard function
#pyautogui.write("Hello World!")
#pyautogui.press('enter',presses=1)
# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#              pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
#pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
# pyautogui.keyDown(key)      #hold the key
#pyautogui.keyUp(key)          #release the key

# Display Box
#pyautogui.alert('This is an alert box.','warning',button='ok')
#a = pyautogui.confirm('Shall I proceed?',buttons=['OK', 'Cancel']))
#print(a)
#print(pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']))
#print(pyautogui.prompt('What is your name?'))
#b = pyautogui.password('Enter password (text will be hidden)', default='', mask='*')
#print(b)


