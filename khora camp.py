import keyboard
import time
import threading

# Function to press a key for a certain duration
def press_key_for_duration(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def ability_1(lock):
    while not exit_flag.is_set():
        with lock:
            press_key_for_duration('1', 0.2)
        time.sleep(3)

def ability_2(lock):
    while not exit_flag.is_set():
        with lock:
            press_key_for_duration('2', 0.5)
        time.sleep(0.5)

def ability_3(lock):
    while not exit_flag.is_set():
        with lock:
            press_key_for_duration('3', 0.5)
        time.sleep(15)

def ability_4(lock):
    while not exit_flag.is_set():
        with lock:
            press_key_for_duration('4', 0.5)
        time.sleep(25)

# Function to set the exit flag when 'x' is pressed
def on_b_pressed(event):
    global exit_flag
    if event.event_type == keyboard.KEY_DOWN:
        exit_flag.set()  # Set the exit flag to stop the loop

# Function to reset the exit flag when 'c' is pressed
def reset(event):
    global exit_flag
    if event.event_type == keyboard.KEY_DOWN:
        exit_flag.clear()  # Clear the exit flag to start the loop

if __name__ == "__main__":
    exit_flag = threading.Event()  # Event to signal when to exit the loop
    lock = threading.Lock()  # Lock for the ability functions

    # Registering event listeners
    keyboard.on_press_key('z', lambda _: [threading.Thread(target=func, args=(lock,)).start() for func in [ability_1, ability_3, ability_4]])
    keyboard.on_press_key('x', on_b_pressed)
    keyboard.on_press_key('c', reset)

    # Wait for the 'esc' key to exit the program
    keyboard.wait('/')
