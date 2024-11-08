#!/usr/bin/env python3
from gpiozero import DistanceSensor, OutputDevice
from time import sleep

# Initialize the DistanceSensor using GPIO Zero library
sensor = DistanceSensor(echo=27, trigger=17)

# Pin Definitions
IN1 = OutputDevice(14)
IN2 = OutputDevice(15)
IN3 = OutputDevice(18)
IN4 = OutputDevice(23)

step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def set_step(w1, w2, w3, w4):
    IN1.value = w1
    IN2.value = w2
    IN3.value = w3
    IN4.value = w4

def step_motor(steps, direction=1, delay=0.0009):
    for _ in range(steps):
        # Check the distance before stepping
        distance = sensor.distance * 100  # Convert to centimeters
        if distance < 20:  # If an object is closer than 20 cm
            print("Object detected within 20 cm. Stopping motor.")
            return  # Exit the function to stop the motor
        for step in (step_sequence if direction > 0 else reversed(step_sequence)):
            set_step(*step)
            sleep(delay)
counter = 0
while True:
    
    step_motor(200, -1)
    print("Moved 15 steps left.")
    sleep(1)  # Short delay between movements
    
    step_motor(200, 1)
    print("Moved 30 steps right.")
    sleep(1)  # Short delay between movements
    counter=1
        

