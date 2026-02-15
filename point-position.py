import pyautogui
import time

# Loop for 10 seconds printing cursor position
start_time = time.time()

while time.time() - start_time < 10:
    x, y = pyautogui.position()
    print(f"Cursor position: X={x}, Y={y}")
    time.sleep(0.5)  # Update every 500ms