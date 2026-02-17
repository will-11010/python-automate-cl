import pyautogui
import time

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
    x = float(proportion_x / screen_width)
    y = float(proportion_y / screen_height)

    print(f"Proporção: ({proportion_x}, {proportion_y}) -> Coordenadas: ({x}, {y})")

    return x, y

# Loop for 10 seconds printing cursor position
start_time = time.time()

while time.time() - start_time < 10:
    x, y = pyautogui.position()
    get_screen_coords(x, y, pyautogui.size()[0], pyautogui.size()[1])
    #print(f"Cursor position: X={x}, Y={y}")
    time.sleep(0.5)  # Update every 500ms