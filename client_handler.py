from constants import *
from button import *
from pyvjoy import VJoyDevice

class Client:
    def __init__(self, j: VJoyDevice):
        self.vjoyDevice = j
        self.buttons = Buttons(j)

    def receive_message(self, message):
        if (message):
            if (message == DISCONNECT_MESSAGE):
                print(f"Disconnected")

            self.process(message)

    def process(self, message: str):
        if message.startswith(BUTTON_KEY):
            decode = message.split(',')
            if decode[0] == BUTTON_KEY:
                try:
                    self.buttons.buttonClick(int(decode[1]), int(decode[2]))
                except:
                    print("Fail")
        else:
            messages = message.split(',')
            try:
                self.updateOrientation(float(messages[1]))
                self.updateAcceleration(float(messages[-2]))
            except:
                print(message + "Error")

    def updateAcceleration(self, value):
        scaled_value = int(value * 32768)
        self.vjoyDevice.data.wAxisZ = scaled_value
        self.vjoyDevice.update()

    def updateOrientation(self, value):
        # Value between -1.5 and 1.5

        if value > 3:
            value = value - CONVERSION_THRESHOLD

        print(value)

        if value >= GYRO_VAL_MAX and value < SKIP_THRESHOLD:
            x_value = X_Y_MIN
            y_value = X_Y_MAX
        elif value < GYRO_VAL_MIN or value > SKIP_THRESHOLD:
            x_value = X_Y_MAX
            y_value = X_Y_MIN
        else:
            oldRange = (GYRO_VAL_MAX - GYRO_VAL_MIN)
            newRange = (X_Y_MAX - X_Y_MIN)
            y_value = (((value - GYRO_VAL_MIN) * newRange) / oldRange) + X_Y_MIN
            x_value = X_Y_MAX - y_value

        self.vjoyDevice.data.wAxisX= int(x_value)
        self.vjoyDevice.update()
        self.vjoyDevice.data.wAxisY= int(y_value)
        self.vjoyDevice.update()