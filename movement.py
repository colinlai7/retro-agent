import pyautogui
import time
import pandas as pd
from tqdm import tqdm
import random

buttonA = "s"
buttonB = "a"
selectButton = "shift"
startButton = "enter"



def clickcenter():
	pyautogui.moveTo(960,540,0.2)
	pyautogui.click()

def up():
	pyautogui.press('up')

def down():
	pyautogui.press('down')

def left():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')

def right():
	pyautogui.press('right')

def aButton():
    pyautogui.keyDown(buttonA)
    pyautogui.keyUp(buttonA)

def bButton():
    pyautogui.press(buttonB)

def selectButton():
    pyautogui.press(selectButton)

def startButton():
    pyautogui.press(startButton)

buttonList = [up, down, left, right, aButton, bButton]
aAndLeft = [aButton, left]

def randomPlay():
    clickcenter()
    count = 0
    while count < 5000:
        time.sleep(.01)
        left()
        aButton()
        count += 1


def selectRandomButton(buttons):
    random.choice(buttons)()

randomPlay()
