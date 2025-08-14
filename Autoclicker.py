import mouse as ms
import time
import keyboard

while True:
    if keyboard.is_pressed('j'):
        # keyboard.press('')

        ms.click('left')
        time.sleep(.001)

#1 You can also change keyboard.is_pressed('j') to another key.

#2 You can change the clicker from using the mouse to keyboard keys by using keyboard.press('').

#3 You can also change the click amount by modifying time.sleep(.001).
