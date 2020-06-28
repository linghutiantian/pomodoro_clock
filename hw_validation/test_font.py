import time

from Adafruit_LED_Backpack import BicolorMatrix8x8

# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8(busnum=2)

digits =[
#0
[0b010, 0b101, 0b101, 0b101, 0b010,],

#1
[0b010, 0b110, 0b010, 0b010, 0b111,],

#2
[0b110, 0b001, 0b010, 0b100, 0b111,],

#3
[0b111, 0b001, 0b011, 0b001, 0b111,],

#4
[0b101, 0b101, 0b111, 0b001, 0b001,],

#5
[0b111, 0b100, 0b111, 0b001, 0b110,],

#6
[0b011, 0b100, 0b111, 0b101, 0b111,],

#7
[0b111, 0b001, 0b010, 0b100, 0b100,],

#8
[0b111, 0b101, 0b111, 0b101, 0b111,],

#9
[0b111, 0b101, 0b111, 0b001, 0b110,],
]


# Three colors are [BicolorMatrix8x8.RED, BicolorMatrix8x8.GREEN, BicolorMatrix8x8.YELLOW]:
def get_digit(x, y, num):
    if (x >= 5):
        return 0
    if y < 3:
        digit = digits[num % 10][x]
        return (digit >> y) & 1
    elif y >= 4 and y <= 6:
        digit = digits[num / 10][x]
        return (digit >> (y - 4) ) & 1
    else:
        return 0

display.begin()

for num in range(26):
    # Clear the display buffer.
    display.clear()

    # Iterate through all positions x and y.
    for x in range(8):
        for y in range(8):
            c = get_digit(x, y, num)
            # Set pixel at position i, j to appropriate color.
            display.set_pixel(x, y, c)
            # Write the display buffer to the hardware.  This must be called to
            # update the actual display LEDs.
    display.write_display()
    # Delay for a quarter second.
    time.sleep(0.25)

