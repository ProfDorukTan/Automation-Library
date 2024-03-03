import time
import pyautogui

pyautogui.FAILSAFE = False

def safetywait():
    time.sleep(0.1)

# Function to move the mouse to a specific position
def move_mouse(x, y):
    pyautogui.moveTo(x, y)
    safetywait()
# Function to move the mouse relative to its current position
def move_mouse_relative(dx, dy):
    current_x, current_y = pyautogui.position()
    new_x = current_x + dx
    new_y = current_y + dy
    pyautogui.moveTo(new_x, new_y)
    safetywait()

# Click functions
def left_click_mouse(button='left'):
    pyautogui.click(button=button)
    safetywait()

def double_click_mouse(button='left'):
    pyautogui.doubleClick(button=button)
    safetywait()

def right_click_mouse():
    pyautogui.rightClick()
    safetywait()

def left_click_mouse_at(x, y, button='left'):
    pyautogui.click(x=x, y=y, button=button)
    safetywait()

def right_click_mouse_at(x, y, button='left'):
    pyautogui.click(x=x, y=y, button=button)
    safetywait()

# Drag functions
def drag_mouse(x, y, duration=1):
    pyautogui.dragTo(x, y, duration=duration)
    safetywait()

def drag_mouse_relative(dx, dy, duration=1):
    current_x, current_y = pyautogui.position()
    new_x = current_x + dx
    new_y = current_y + dy
    pyautogui.dragTo(new_x, new_y, duration=duration)
    safetywait()


# Function to scroll the mouse
def scroll_mouse(amount):
    pyautogui.scroll(amount)
    safetywait()
