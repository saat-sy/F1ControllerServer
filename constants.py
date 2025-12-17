PORT = 1234
HEADER = 20
DECODE_FORMAT = "utf-8"
DISCONNECT_MESSAGE = "Disconnect"
ACC, BRAKE, G_UP, G_DOWN, KERS, DRS = 1, 2, 3, 4, 5, 6
BUTTON_KEY = "B"
ORIENTATION_KEY = "O"
MIN_BUTTON_SYNTAX_LEN = 5
X_Y_MIN = 0
X_Y_MAX = 32768

# Gyro values
# 0 - 3 --> 0 - 3
# 3 - 4 and -1.5 - 0 --> 0 - -3 

GYRO_VAL_MIN = -2
GYRO_VAL_MAX = 2
SKIP_THRESHOLD = 4 # When the value jumps to 4 directly
CONVERSION_THRESHOLD = 6.27
HORIZONTAL_BIAS = 0.03

# Button syntax:
# B, Button_Num, 1/0 - State