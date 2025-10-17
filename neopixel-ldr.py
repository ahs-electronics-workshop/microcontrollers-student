import time
import board
import neopixel
import digitalio
from analogio import AnalogIn, AnalogOut

# read voltage on LDR circuit at the voltage divider. What is pin your analog in pin?
# ldr_in = AnalogIn(board.A4)
ldr_in = ...

# set D5(power to LDR circuit) to high
ldr = digitalio.DigitalInOut(board.D5) 
ldr.direction = digitalio.Direction.OUTPUT
ldr.value = True

# neopixel circuit -- D1 writes to neopixel
# what digital pin is writing to the neopixel?
# How many neopixels?
led = neopixel.NeoPixel(board.D1, 1)
led.brightness = 0.3
while True:
    print(ldr_in.value)
    # decide the value
    if ... <...:
        # light your neopixel
        # the way you want
        led [0] = (255, 0, 0)
    else:
        led [0] = (0,0,0)