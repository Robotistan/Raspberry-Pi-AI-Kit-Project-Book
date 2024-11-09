import gpiod
import time

LED_PIN_G = 17
LED_PIN_Y = 27
LED_PIN_R = 22

chip = gpiod.Chip('gpiochip4')

led_lineG = chip.get_line(LED_PIN_G)
led_lineG.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

led_lineY = chip.get_line(LED_PIN_Y)
led_lineY.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

led_lineR = chip.get_line(LED_PIN_R)
led_lineR.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

while True:
    led_lineG.set_value(0)
    led_lineY.set_value(0)
    led_lineR.set_value(1)
    time.sleep(3)
    
    led_lineG.set_value(0)
    led_lineY.set_value(1)
    led_lineR.set_value(0)
    time.sleep(0.5)
    
    led_lineG.set_value(1)
    led_lineY.set_value(0)
    led_lineR.set_value(0)
    time.sleep(2)
