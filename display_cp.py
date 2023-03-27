import board
from adafruit_ht16k33.matrix import Matrix8x8x2

digits =[
[0b010, 0b101, 0b101, 0b101, 0b010,],#0 
[0b010, 0b110, 0b010, 0b010, 0b111,],#1 
[0b110, 0b001, 0b010, 0b100, 0b111,],#2 
[0b111, 0b001, 0b011, 0b001, 0b111,],#3 
[0b101, 0b101, 0b111, 0b001, 0b001,],#4 
[0b111, 0b100, 0b111, 0b001, 0b110,],#5 
[0b011, 0b100, 0b111, 0b101, 0b111,],#6 
[0b111, 0b001, 0b010, 0b100, 0b100,],#7 
[0b111, 0b101, 0b111, 0b101, 0b111,],#8 
[0b111, 0b101, 0b111, 0b001, 0b110,],#9 
]

class Display(object):
    def __init__(self, busnum=1):
        i2c = board.I2C()
        self.matrix = Matrix8x8x2(i2c)

    def ShowTime(self, minutes, seconds, point1_seconds,
            main_color=None,
            pause=False,
            pause_color=None,
            off_color=None):
        if main_color is None:
            main_color=self.matrix.LED_GREEN
        if pause_color is None:
            pause_color=self.matrix.LED_YELLOW
        if off_color is None:
            off_color=self.matrix.LED_OFF
        for x in range(8):
            for y in range(8):
                c = self._GetPixel(x, y, minutes, seconds, point1_seconds,
                        main_color, pause, pause_color, off_color)
                self.matrix[y,x] = c

    def _GetPixel(self, x, y, minutes, seconds, point1_seconds, main_color, pause, pause_color,
            off_color):
        if minutes > 99:
            minutes = 99
        c = main_color
        if (x == 7):
            if pause:
                return pause_color
        if (x == 6):
            if not pause:
                if point1_seconds < 5:
                    seconds = seconds - 8
            if y * 7.5 > seconds:
                return off_color
            else:
                return c
        if (x >= 5):
            return off_color
        if y < 3:
            digit = digits[minutes % 10][x]
            return c if (digit >> y) & 1 else 0
        elif y >= 4 and y <= 6:
            digit = digits[minutes // 10][x]
            return c if (digit >> (y - 4) ) & 1 else 0
        else:
            return off_color

