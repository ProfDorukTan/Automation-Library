import pyautogui
import pygetwindow

# Get the target window by its title
target_window_title = "Your Window Title"
target_window = pygetwindow.getWindowsWithTitle(target_window_title)[0]

# Activate the target window
target_window.activate()

# Get the coordinates of the button within the target window
button_x = target_window.left + 100  # Adjust these values as needed
button_y = target_window.top + 50    # Adjust these values as needed

# Move the mouse to the button's coordinates within the target window
pyautogui.moveTo(button_x, button_y)

# Perform a mouse click operation
pyautogui.click()
