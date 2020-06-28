import Adafruit_BBIO.GPIO as GPIO

import time
from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import BicolorMatrix8x8

GPIO.setup("P9_12", GPIO.IN)

display = BicolorMatrix8x8.BicolorMatrix8x8(busnum=2)

display.begin()

# Run through each color and pixel.
# Iterate through all colors.
while True:
  for c in [BicolorMatrix8x8.RED, BicolorMatrix8x8.GREEN, BicolorMatrix8x8.YELLOW]:
      # Iterate through all positions x and y.
      for x in range(8):
          for y in range(8):
              # Clear the display buffer.
              display.clear()
              # Set pixel at position i, j to appropriate color.
              display.set_pixel(x, y, c)
              # Write the display buffer to the hardware.  This must be called to
              # update the actual display LEDs.
              display.write_display()
              GPIO.wait_for_edge("P9_12", GPIO.RISING)

