import pygetwindow
import time

from LogPanel import LogPanel
import MauseAutomation 
import KeyboardAutomation
from ImageAutomation import ImageAutomation


if __name__ == "__main__":
    panel = LogPanel()
    panel.log_info("Starting the automation script...")
    panel.log_warning("This is a warning message.")
    panel.log_error("This is an error message.")
    panel.log_success("This is a success message.")

    # Get all active windows with names
    active_windows = [window for window in pygetwindow.getAllTitles() if window]

    # Map all active windows to their number i
    window_map = {i: window for i, window in enumerate(active_windows, start=1)}

    # Print the names of all active windows with their numbers
    for i, window in window_map.items():
        panel.log_info("Open window {}: {}".format(i, window))

    # Ask user to choose a window to automate
    selected_window = None
    while not selected_window:
        try:
            window_number = int(input("Enter the number of the window you want to automate: "))
            selected_window = window_map.get(window_number)
            if not selected_window:
                panel.log_error("Invalid window number. Please try again.")
        except ValueError:
            panel.log_error("Invalid input. Please enter a valid window number.")

    # Perform automation on the selected window
    if selected_window:
        panel.log_info("Automating window: {}".format(selected_window))
        image_automation = ImageAutomation(window=selected_window)
        image_automation.capture_window_screenshot()
        # Attempt to get the position of the image
        for i in range(10):
            position = image_automation.get_image_position("edit2.png", 0.9)
            if position is not None:
                x, y = position
                panel.log_success("Found the image at position: " + str(x) + " " + str(y))
                MauseAutomation.move_mouse(x, y)
            else:
                panel.log_error("Image not found.")


        #DO SOME AUTOMATION
        #DO SOME AUTOMATION
        #DO SOME AUTOMATION
        #DO SOME AUTOMATION
        #DO SOME AUTOMATION
        #DO SOME AUTOMATION

        



    else:
        panel.log_info("No window selected. Automation terminated.")