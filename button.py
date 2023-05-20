from typing import List
from constants import *
from pyvjoy import VJoyDevice
import pyvjoy

class Button:
    def __init__(self, id):
        self.id = id
        self.pressed = False

    def state(self, state: int):
        self.pressed = True if state == 1 else False

class Buttons:
    def __init__(self, j: VJoyDevice) -> None:
        self.buttons: List[Button] = [
            Button(ACC),
            Button(BRAKE),
            Button(G_UP),
            Button(G_DOWN)
        ]
        self.vjoyDevice = j

    def buttonClick(self, buttonId, state):
        for button in self.buttons:
            if button.id == buttonId:
                button.state(state)
                break
        self.updateVjoy()

    def updateVjoy(self):
        activeButtons = 0
        for button in self.buttons:
            if button.pressed:
                activeButtons += pow(2, button.id)

        self.vjoyDevice.data.lButtons = activeButtons
        self.vjoyDevice.update()