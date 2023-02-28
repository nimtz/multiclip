import pyperclip
import keyboard
import time
from os import system

system("title " + "multiclip")

secondary_clipboards = ["", "", "", "", "", "", "", "", "", "", "", ""]
print("Ctrl+Shift+F1 to 12 to store")
print("Ctrl+Win+F1 to 12 to retrieve")

def copy(index):
    global secondary_clipboards
    keyboard.release('shift')
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.01)
    text = pyperclip.paste()
    secondary_clipboards[index - 1] = text
    print("F"+str(index),":",text)

def paste(index):
    global secondary_clipboards
    pyperclip.copy(secondary_clipboards[index - 1])
    keyboard.release('windows')
    keyboard.press_and_release('v')
        
def register_hotkeys():
    for i in range(1, 13):
        keyboard.add_hotkey(f'ctrl+shift+F{i}', lambda index=i: copy(index))
        keyboard.add_hotkey(f'ctrl+windows+F{i}', lambda index=i: paste(index))

if __name__ == '__main__':
    register_hotkeys()
    keyboard.wait()
