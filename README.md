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

## Dev Container (VS Code)

Este projeto inclui uma configuração de **Dev Container** para padronizar o ambiente de desenvolvimento (Python, extensões do VS Code e dependências de interface gráfica como `scrot` e `xclip`).

### Como usar

1. Certifique-se de ter o **Docker Desktop** rodando e a extensão **Dev Containers** instalada no VS Code.
2. **Ajuste para Linux/Interface Gráfica:** No Docker Desktop, vá em *Settings ⚙️ -> Resources -> File Sharing* e adicione o caminho `/tmp/.X11-unix` (necessário para o PyAutoGUI interagir com sua tela).
3. Abra esta pasta no VS Code.
4. Quando solicitado, clique em **Reopen in Container** (ou abra a Paleta de Comandos com `Ctrl+Shift+P` e digite `Dev Containers: Reopen in Container`).

O VS Code vai buildar o ambiente e instalar o `requirements.txt` automaticamente.

### What is included

- Python 3.11 base image
- Linux dependencies used by this project (`python3-tk`, `python3-dev`, `scrot`, `xclip`)
- Automatic install of Python packages from `requirements.txt`
- Recommended VS Code extensions for Python and Pylance

### How to use

1. Install Docker and the VS Code extension **Dev Containers**.
2. Open this project in VS Code.
3. Run command: `Dev Containers: Reopen in Container`.
4. Wait for the image build and post-create setup.

After this, the workspace runs fully inside the container with the project dependencies preconfigured.

## Safety Notes

- PyAutoGUI has a failsafe feature (move mouse to corner to interrupt)
- Always test scripts carefully before running
- Use delays (`pyautogui.PAUSE` or `time.sleep`) between actions to prevent issues
- Be cautious with automated mouse/keyboard input

## Project Structure

```
python-automate/
├── .devcontainer/
│   ├── devcontainer.json  # Dev Container configuration
│   └── Dockerfile         # Container image definition
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