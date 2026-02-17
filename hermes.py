#!/usr/bin/env python3
"""
Main automation script using pyautoguifile_017

"""

import time
import argparse
import pyautogui

# Safety features - enable fail-safe by moving mouse to corner
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1  # Pause between actions to avoid race conditions


def get_screen_coords(proportion_x, proportion_y, screen_width, screen_height):
    """Converte proporções de tela (0-1) para pixel coordinates
    
    Args:
        proportion_x: Proporção horizontal (0.0 a 1.0)
        proportion_y: Proporção vertical (0.0 a 1.0)
        screen_width: Largura da tela em pixels
        screen_height: Altura da tela em pixels
    
    Returns:
        Tuple (x, y) com as coordenadas em pixels
    """
    x = int(screen_width * proportion_x)
    y = int(screen_height * proportion_y)
    return x, y


def main(url):
    """Main entry point for automation script
    
    Args:
        url: Website URL to open in browser (initial page)
    """
    print("Starting automation...")
    print(f"Initial URL: {url}")

    # Variables of time
    time_to_wait_for_page_load = 4  # Time to wait for page to load (adjust as needed)
    time_to_wait_for_download = 4  # Time to wait for download to complete (adjust as needed)
    
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    print(f"Screen size: {screen_width}x{screen_height}")

    # Focus on Opera window (already open) - click on the window area
    time.sleep(1)
    x, y = get_screen_coords(0.5, 0.5, screen_width, screen_height)
    pyautogui.click(x=x, y=y)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)

    # Open new tab and navigate to initial URL
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    
    print(f"Opening initial page: {url}")
    pyautogui.write(url, interval=0.01)
    pyautogui.press('enter')
    time.sleep(6)

    # Get initial URL for comparison
    initial_url = url.rstrip('/')
    page_count = 0

    # Loop through pages by clicking next button until URL changes back to initial
    while True:
        page_count += 1
        print(f"\nProcessing page {page_count}")
        
        # Click on page content to load (if needed)
        x, y = get_screen_coords(0.702, 0.623, screen_width, screen_height)
        pyautogui.click(x=x, y=y)
        time.sleep(1)

        # Click on extension | TODO: Automate this part by finding the extension icon on the screen
        x, y = get_screen_coords(0.956, 0.08, screen_width, screen_height)
        pyautogui.click(x=x, y=y)
        time.sleep(time_to_wait_for_download)

        # Download file | TODO: Automate this part by finding the download button on the screen
        print(pyautogui.position())
        x, y = get_screen_coords(0.736, 0.221, screen_width, screen_height)
        pyautogui.click(x=x, y=y)
        time.sleep(0.5)
        x, y = get_screen_coords(0.868, 0.142, screen_width, screen_height)
        pyautogui.click(x=x, y=y)
        time.sleep(2)
        # Write page number as file name with 3 digits
        pyautogui.write(f"file_{page_count - 1:03d}", interval=0.01)
        pyautogui.press('enter')
        time.sleep(1)

        # Close download tab
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)

        # Click next button to go to next page
        print(f"Clicking next button to go to page {page_count + 1}")
        x, y = get_screen_coords(0.619, 0.135, screen_width, screen_height)
        pyautogui.click(x=x, y=y)
        time.sleep(time_to_wait_for_page_load)

        # Check current URL
        try:
            import subprocess
            
            # Select and copy the URL from address bar
            pyautogui.hotkey('ctrl', 'l')  # Select address bar
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'c')  # Copy URL
            time.sleep(0.3)
            
            # Get clipboard content using xclip
            result = subprocess.run(
                ["xclip", "-selection", "clipboard", "-o"],
                capture_output=True,
                text=True
            )
            current_url = result.stdout.strip()
            print(f"Current URL: {current_url}")
            
            # Check if we're back at the initial page
            if page_count > 1:  # Only consider it a loop after processing at least 2 pages
                # Remove trailing slashes for comparison
                normalized_current = current_url.rstrip('/')
                normalized_initial = initial_url.rstrip('/')
                
                # If current URL matches initial URL EXACTLY, we've completed the cycle
                if normalized_current == normalized_initial:
                    x, y = get_screen_coords(0.433, 0.194, screen_width, screen_height)
                    pyautogui.click(x=x, y=y)
                    time.sleep(1)
                    print(f"\nCompleted cycle: Returned to initial URL after {page_count} page(s)")
                    break
        except Exception as e:
            print(f"Error checking URL: {e}")
            pass

    print(f"\nAutomation complete! Processed {page_count} page(s)")


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
