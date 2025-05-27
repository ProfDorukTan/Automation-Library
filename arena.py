import keyboard
import time
import KeyboardAutomation as ka
import threading

# Function to press a key for a certain duration
def press_key_for_duration(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def melee():
    while not exit_flag.is_set():  # Loop until the exit flag is set
        press_key_for_duration(';', 0.2)

def ability():
    while not exit_flag.is_set():  # Loop until the exit flag is set
        press_key_for_duration('1', 0.2)
        time.sleep(5)
        time.sleep(5)

def soulform():
    while not exit_flag.is_set():  # Loop until the exit flag is set
        with soulform_lock:
            time.sleep(0.5)
            press_key_for_duration('5', 0.2)
            press_key_for_duration('2', 0.3)
            press_key_for_duration('5', 0.2)
            time.sleep(0.5)
        time.sleep(30)


# Function to set the exit flag when 'b' is pressed
def on_b_pressed(event):
    global exit_flag
    if event.event_type == keyboard.KEY_DOWN:
        exit_flag.set()  # Set the exit flag to stop the loop

def reset(event):
    global exit_flag
    if event.event_type == keyboard.KEY_DOWN:
        exit_flag.clear()  # Set the exit flag to stop the loop

if __name__ == "__main__":
    exit_flag = threading.Event()  # Event to signal when to exit the loop
    soulform_lock = threading.Lock()  # Lock for soulform function

    # Registering event listeners
    keyboard.on_press_key('z', lambda _: [threading.Thread(target=func).start() for func in [melee, ability]])
    keyboard.on_press_key('x', on_b_pressed)
    keyboard.on_press_key('c', reset)

    # Wait for the 'esc' key to exit the program
    keyboard.wait('/')
