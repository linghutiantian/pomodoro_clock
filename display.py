from Adafruit_LED_Backpack import BicolorMatrix8x8

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
        self.display = BicolorMatrix8x8.BicolorMatrix8x8(busnum=busnum)
        self.display.begin()
    def ShowTime(self, minutes, seconds, point1_seconds, main_color=BicolorMatrix8x8.GREEN, pause=False,
            pause_color=BicolorMatrix8x8.YELLOW):
        self.display.clear()
        for x in range(8):
            for y in range(8):
                c = self._GetPixel(x, y, minutes, seconds, point1_seconds,
                        main_color, pause, pause_color)
                self.display.set_pixel(x, y, c)
        self.display.write_display()

    def _GetPixel(self, x, y, minutes, seconds, point1_seconds, main_color, pause, pause_color):
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
                return 0
            else:
                return c
        if (x >= 5):
            return 0
        if y < 3:
            digit = digits[minutes % 10][x]
            return c if (digit >> y) & 1 else 0
        elif y >= 4 and y <= 6:
            digit = digits[minutes / 10][x]
            return c if (digit >> (y - 4) ) & 1 else 0
        else:
            return 0

