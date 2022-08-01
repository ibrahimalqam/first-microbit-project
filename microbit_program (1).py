# Add your Python code here. E.g.
from microbit import *
import radio
radio.config(group=5)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('I AM SENDING')
