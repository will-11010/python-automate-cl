#!/usr/bin/env python3
"""
Main automation script using pyautogui
"""

import time
import argparse
import pyautogui

# Safety features - enable fail-safe by moving mouse to corner
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1  # Pause between actions to avoid race conditions


def main(url):
    """Main entry point for automation script
    
    Args:
        url: Website URL to open in browser
    """
    print("Starting automation...")
    print("Example: Getting screen size...")
    
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    print(f"Screen size: {screen_width}x{screen_height}")
    
    # Get current mouse position
    current_x, current_y = pyautogui.position()

    # Alt + Tab para trocar de janela
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 't')
    # Insert link to open
    print(f"Opening URL: {url}")
    pyautogui.write(url, interval=0.01)
    pyautogui.press('enter')
    time.sleep(2)

    # Print mouse position
    print(pyautogui.position())
     # Get current mouse position
    current_x, current_y = pyautogui.position()

    # Loop 10 times to download files
    for i in range(10):
        # Click on extension | TODO: Automate this part by finding the extension icon on the screen
        pyautogui.click(x=1303, y=62)
        time.sleep(10)

        # Download file | TODO: Automate this part by finding the download button on the screen
        print(pyautogui.position())
        pyautogui.click(x=1006, y=170)
        time.sleep(0.5)
        pyautogui.click(x=1191, y=116)
        time.sleep(2)
        # Write i position as file name with 3 digits
        pyautogui.write(f"file_{i:03d}", interval=0.01) 
        pyautogui.press('enter')

        # Close downloaded file tab
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'w')

    # Click on Download button | TODO: Automate this part by finding the download button on the screen

    pyautogui.hotkey('alt', 'tab')
    
    print("Automation complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Automate browser navigation using pyautogui'
    )
    parser.add_argument(
        'url',
        help='URL to open in the browser'
    )
    
    args = parser.parse_args()
    main(args.url)
