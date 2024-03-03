import pyautogui
import time

def safetywait():
    time.sleep(0.1)

def type_text(text):
    pyautogui.typewrite(text)
    safetywait()

def press_key(key):
    pyautogui.press(key)
    safetywait()

def hold_key(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    safetywait()

#Non-letter key functions
def press_enter():
    pyautogui.press('enter')
    safetywait()

def press_tab():
    pyautogui.press('tab')
    safetywait()

def press_backspace():
    pyautogui.press('backspace')
    safetywait()

def press_delete():
    pyautogui.press('delete')
    safetywait()

def press_escape():
    pyautogui.press('escape')
    safetywait()

def press_space():
    pyautogui.press('space')
    safetywait()

#Hotkey functions
def hotkey_ctrl_c():
    pyautogui.hotkey('ctrl', 'c')
    safetywait()

def hotkey_ctrl_v():
    pyautogui.hotkey('ctrl', 'v')
    safetywait()

def hotkey_ctrl_x():
    pyautogui.hotkey('ctrl', 'x')
    safetywait()

def hotkey_ctrl_z():
    pyautogui.hotkey('ctrl', 'z')
    safetywait()

def hotkey_ctrl_y():
    pyautogui.hotkey('ctrl', 'y')
    safetywait()

def hotkey_ctrl_s():
    pyautogui.hotkey('ctrl', 's')
    safetywait()

def hotkey_ctrl_a():
    pyautogui.hotkey('ctrl', 'a')
    safetywait()

def hotkey_ctrl_f():
    pyautogui.hotkey('ctrl', 'f')
    safetywait()

def hotkey_ctrl_p():
    pyautogui.hotkey('ctrl', 'p')
    safetywait()

def hotkey_ctrl_o():
    pyautogui.hotkey('ctrl', 'o')
    safetywait()
