import network
import socket
import time
from machine import Pin, I2C, PWM
from time import sleep
from picobricks import SSD1306_I2C

led = Pin(7, Pin.OUT)
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)
pin_button = Pin(10, Pin.IN, Pin.PULL_UP)  # Configured button with pull-up
buzzer = PWM(Pin(20))

person_count = 0
car_count = 0
#scissors_count = 0

# Wi-Fi settings
SSID = 'MY_SSID'      # Enter your Wi-Fi SSID
PASSWORD = 'PASSWORD' # Enter your Wi-Fi password

# Start Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Wait for Wi-Fi connection
while not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Wi-Fi Connection successful:", wlan.ifconfig())
