import time
import board
import neopixel
import random


pixel_pin = board.D5
num_pixels = 2
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
   pixel_pin,
   num_pixels,
   brightness=.3,
   auto_write=False,
   pixel_order=ORDER
)

# this returns 3 random numbers
# between 0 and 255 (RGB values)
# return a tuple (r, g, b)
def random_color():
   r = ...
   g = ...
   b = ...
   return (r, g, b)

# set each individual pixel to a 
# random color
def light_up(wait):
   for i in range(num_pixels):
       pixels[i] = ...
   pixels.show()
   time.sleep(wait)

while True:
   #fills all red
   pixels.fill((255, 0, 0))
   pixels.show()
   time.sleep(1)
   # fill all green
   ...
   # fill all blue
   ...

   light_up(0.5)
