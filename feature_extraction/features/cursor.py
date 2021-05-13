import pyautogui
import numpy as np
import math


class cursor(object):
    
    def __init__(self, freq):
        self.freq = freq
        
    def move_cursor(self,input_data):        
        # inp = input_data
        # up = input_data[2,1]
        # down = input_data[6,1]
        # right = input_data[1,1]
        # left = input_data[3,1]
        up = np.mean(input_data[5, -50:]) #5
        down = np.mean(input_data[2, -50:]) #2
        right = np.mean(input_data[0, -50:]) #0
        left = np.mean(input_data[4, -50:]) #4
        pyautogui.move(up-down, right-left,duration=1/self.freq)
        #pyautogui.move(self.down, self.right, duration=0.005)


        #pyautogui,move(100,100)

# def cursor(mav_data)
    # screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    # currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    # pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    # pyautogui.click() # Click the mouse at its current location.
    # pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    # pyautogui.doubleClick() # Double click the mouse at the
    
# #------------------move--------    
    # pyautogui.move(0, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    
    # pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    # pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    
    
    # pyautogui.press('esc') # Simulate pressing the Escape key.
    # pyautogui.keyDown('shift')
    # pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    # pyautogui.keyUp('shift')
    # pyautogui.hotkey('ctrl', 'c')
