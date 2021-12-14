"""
Copies the webpage currently open in firefox dev and pastes to a file
"""

from pyautogui import hotkey, typewrite, press
from pyperclip import paste
from datetime import datetime

hotkey('command', 'space')
typewrite('firefox dev')
press('enter')
hotkey('command', 'a')
hotkey('command', 'c')
copied = paste()

dt = datetime.now()

formatted_dt = str(dt).replace(' ', '_')

print(formatted_dt)

with open(f'./files/{formatted_dt}.txt', 'w') as file:
    file.write(copied)
