# F1 Controller Server

Simulates joystick input using the VJoy virtual joystick driver.

## Requirements

- **VJoy**: The VJoy driver must be installed and configured on your system. [Download VJoy](https://sourceforge.net/projects/vjoystick/)
- **Python**: Python 3.7 or newer.
- **Python Packages**:  
    - [`pyvjoy`](https://pypi.org/project/pyvjoy/) (for direct VJoy device control)

Install dependencies with:
```bash
pip install pyvjoy
```

## Overview

This module is designed specifically for use with the F1 game, allowing for programmatic control of a virtual joystick to simulate controller input. It enables automated input for testing, custom control schemes, or remote control of the game.

**Important:** To use this server, you must also install the companion Android app, which acts as the controller interface. The app sends commands to this server, which then simulates joystick input for the F1 game.

## Usage

1. Ensure VJoy is installed and at least one virtual device is configured.
2. Install the required Python packages.
3. Import and use the module in your Python scripts to send joystick commands.

Example:
```python
import pyvjoy

j = pyvjoy.VJoyDevice(1)
j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)  # Move X axis to mid position
```

## Disclaimer

This project is not affiliated with VJoy or any game developer. Use at your own