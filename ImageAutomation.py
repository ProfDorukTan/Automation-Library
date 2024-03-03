import os
import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import win32gui
import win32con
import time
from LogPanel import LogPanel

panel = LogPanel()
def get_app_dict(handles={}):
    win32gui.EnumWindows(window_enum_handler, handles)
    return handles

def window_enum_handler(hwnd, handle_dict):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        handle_dict[win32gui.GetWindowText(hwnd)] = hwnd

class ImageAutomation:
    def __init__(self, window):
        self.window = window
        

    def capture_window_screenshot(self, save_path="images/window_screenshot.png"):
        # Get the window to the top
        app_dict = get_app_dict()
        handle = app_dict.get(self.window)
        win32gui.ShowWindow(handle, win32con.SW_RESTORE)
        win32gui.SetWindowPos(handle,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
        win32gui.SetWindowPos(handle,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
        win32gui.SetWindowPos(handle,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        time.sleep(0.5) # Wait for the window to come to the top
        
        # Get the window object by its title - for screenshot capture
        window = gw.getWindowsWithTitle(self.window)
        if window:
            # Get the position and size of the window
            left, top, width, height = window[0].left, window[0].top, window[0].width, window[0].height
            # Capture the screenshot of the window
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save(save_path)
            panel.log_success(f"Screenshot saved to: {save_path}")
            return screenshot
        else:
            panel.log_error(f"Window with title '{self.window}' not found.")
            
    def get_image_position(self, image_name, threshold=0.8):
        # Construct the image path
        image_path = os.path.join("images", image_name)
        # Load the image to search for
        template = cv2.imread(image_path)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Get the dimensions of the template image
        h, w = template_gray.shape[::-1]

        # Capture a screenshot of the window
        self.capture_window_screenshot()
        screenshot_path = "images/window_screenshot.png"
        screenshot = cv2.imread(screenshot_path)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

        # Threshold to consider a match
        loc = np.where(res >= threshold)

        if loc[0].size > 0:  # Check if any matches were found
            # Calculate the center point of the matched region
            center_x = int((loc[1][0] + loc[1][-1] + w) / 2)
            center_y = int((loc[0][0] + loc[0][-1] + h) / 2)
            return center_x, center_y
        else:
            return None

    


