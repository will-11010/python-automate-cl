# Python Automate - GUI Automation with PyAutoGUI

A Python project for automating GUI interactions using PyAutoGUI.

## Features

- Mouse and keyboard automation
- Screenshot and image analysis
- Cross-platform GUI control
- Simple, modular scripts

## Requirements

- Python 3.8+
- pyautogui
- pillow
- pynput

## Installation

1. Create a virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   apt-get install python3-tk python3-dev
   ```

## Usage

Run the main script with url parameter:
```bash
python main.py "<URL>"
```

## Safety Notes

- PyAutoGUI has a failsafe feature (move mouse to corner to interrupt)
- Always test scripts carefully before running
- Use delays (`pyautogui.PAUSE` or `time.sleep`) between actions to prevent issues
- Be cautious with automated mouse/keyboard input

## Project Structure

```
python-automate/
├── main.py              # Main automation script
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .github/
    └── copilot-instructions.md  # Copilot configuration
```

## Examples

See `main.py` for basic examples of:
- Getting screen size
- Getting mouse position
- Basic setup for automation scripts