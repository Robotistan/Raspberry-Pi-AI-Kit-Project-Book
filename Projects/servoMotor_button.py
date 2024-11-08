from gpiozero import Servo
from time import sleep
import gpiod

# GPIO pin for the servo
myGPIO = 17
BUTTON_PIN_R = 16

chip = gpiod.Chip('gpiochip4')

button_line = chip.get_line(BUTTON_PIN_R)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

# Correction factor for the servo
myCorrection = 0.45
maxPW = (2.0 + myCorrection) / 1000  # Maximum pulse width
minPW = (1.0 - myCorrection) / 1000  # Minimum pulse width

# Initialize the servo with adjusted pulse width range
servo = Servo(myGPIO, min_pulse_width=minPW, max_pulse_width=maxPW)

# Continuously move servo between positions
while True:
    button_state = button_line.get_value()
    #print(button_state)
    #sleep(0.2)
    sleep(0.1)
    if button_state == 1:
        servo.max()
        print("max")
        
    else:
        servo.min()
        print("min")
        