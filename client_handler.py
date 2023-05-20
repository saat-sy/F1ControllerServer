import socket
from constants import *
from button import *
from pyvjoy import VJoyDevice

class Client:
    def __init__(self, connection: socket.socket, address: tuple, j: VJoyDevice):
        self.connection = connection
        self.address = address
        self.vjoyDevice = j
        self.buttons = Buttons(j)

    def recieve_messages(self):
        while True:
            message = self.connection.recv(HEADER).decode(DECODE_FORMAT)
            if (message):
                if (message == DISCONNECT_MESSAGE):
                    print(f"Disconnected: {self.address}")
                    break

                self.process(message)
                # print(message)


        self.close()

    def process(self, message: str):
        if message.startswith(BUTTON_KEY):
            messages = [message[i:i+MIN_BUTTON_SYNTAX_LEN] for i in range(0, len(message), MIN_BUTTON_SYNTAX_LEN)]
            for m in messages:
                decode = m.split(',')
                if decode[0] == BUTTON_KEY:
                    try:
                        self.buttons.buttonClick(int(decode[1]), int(decode[2]))
                    except:
                        print("Fail")
        else:
            messages = message.split(',')
            try:
                starting = messages.index(ORIENTATION_KEY)
            except:
                return
            for i in range(starting+1, len(messages), 2):
                try:
                    self.updateOrientation(float(messages[i]))
                except:
                    print(message)
                    continue

    def updateOrientation(self, value):
        # Value between -1.5 and 1.5
        if value > GYRO_VAL_MAX:
            x_value = X_Y_MIN
            y_value = X_Y_MAX
        elif value < GYRO_VAL_MIN:
            x_value = X_Y_MAX
            y_value = X_Y_MIN
        else:
            oldRange = (GYRO_VAL_MAX - GYRO_VAL_MIN)
            newRange = (X_Y_MAX - X_Y_MIN)
            y_value = (((value - GYRO_VAL_MIN) * newRange) / oldRange) + X_Y_MIN
            x_value = X_Y_MAX - y_value

        print(x_value, y_value)
        self.vjoyDevice.data.wAxisX= int(x_value)
        self.vjoyDevice.update()
        self.vjoyDevice.data.wAxisY= int(y_value)
        self.vjoyDevice.update()

    def close(self):
        self.connection.close()