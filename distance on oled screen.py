'''
Example: Measure distance using Ultrasonic sensor and display results on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

# default pins in Ultrasonic class are:
# trigger: pin13
# echo: pin15

ultrasonic_sensor = Ultrasonic()
initialize()
clear_oled()
# or
# ultrasonic_sensor = Ultrasonic(trig=pin13, echo=pin15)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    add_text(0, 0, str(int(distance_value)))
    add_text(0, 1, "Hi")
    add_text(0, 2, "------")
    add_text(0, 3, "ibrahim")
