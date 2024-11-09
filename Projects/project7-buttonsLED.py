import gpiod
import time

LED_PIN_R = 18
BUTTON_PIN = 16

chip = gpiod.Chip('gpiochip4')

led_lineR = chip.get_line(LED_PIN_R)
led_lineR.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

button_line = chip.get_line(BUTTON_PIN)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

while True:
    button_state = button_line.get_value()
    print(button_state)
    
    if button_state == 1:  # Assuming the button is active-low
        led_lineR.set_value(1)
    else:
        led_lineR.set_value(0)

    time.sleep(0.1)  # Sleep for a short duration to avoid busy waiting and CPU usage
