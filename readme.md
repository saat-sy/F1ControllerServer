F1ControllerServer
===================

## Overview

F1ControllerServer is built with Python and leverages the vJoy virtual joystick driver to emulate a physical game controller. The server communicates over UDP, allowing remote devices such as mobile apps or custom clients to send control commands (button presses, axis movements) to the server. These commands are then translated into joystick actions using the `pyvjoy` library, which provides a Python interface to vJoy (note: vJoy is Windows-only).

## How It Works

1. **Remote Client Communication**: A client (such as a mobile app) sends UDP packets containing control data to the server. These packets typically encode button states, axis positions, and other control information.
2. **Message Decoding**: The server receives each UDP packet, decodes the message, and determines the intended joystick action (e.g., which button to press, how to move the steering axis).
3. **Virtual Joystick Update**: Using `pyvjoy`, the server updates the state of the vJoy device to reflect the received commands. This emulates a real controller, allowing games or simulators to respond as if a physical device was connected.
4. **Real-Time Control**: The process is repeated in real time, enabling smooth and responsive remote control of the game or simulator.

## Usage Instructions

1. **Install Python Dependencies**
    Make sure you have Python 3.7 or newer installed. Then, install required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. **Install and Configure vJoy**
    Download and install vJoy from [here](https://sourceforge.net/projects/vjoystick/). Configure at least one virtual joystick device using the vJoy configuration tool. (This step is required only on Windows.)

3. **Start the Server**
    Run the server script to begin listening for UDP messages:
    ```sh
    python server.py
    ```


4. **Connect a Client**
    You can use the companion Android app to control the server. 
    
    Download it from:
    [F1ControllerAndroidApp on GitHub](https://github.com/saat-sy/F1ControllerAndroidApp)
    
    
    The app provides a user-friendly interface for sending control commands to the server over UDP. Alternatively, you may use a custom script or another compatible client to send UDP messages to the server's IP and port. The message format should match what the server expects (see code for details).

5. **Control the Game**
    Once connected, the server will translate incoming messages into joystick actions, allowing you to control games or simulators remotely and programmatically.

## Additional Notes
- This solution is designed for Windows systems due to the vJoy dependency. pyvjoy and vJoy will not work on Linux or macOS.
- The project enables remote, automated, or custom control of games by emulating a physical controller, making it useful for testing, accessibility, or creative control schemes.
- Message formats and button mappings are defined in the server code and should be matched by the client.