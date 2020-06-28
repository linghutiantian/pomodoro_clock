import time
import math
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_LED_Backpack import BicolorMatrix8x8


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

GPIO.setup("P9_12", GPIO.IN)

class Pomo:

    # States
    WORK_PAUSE = 0
    WORK_RUN = 1
    REST_PAUSE = 2
    REST_RUN = 3
    
    
    # Some constants
    NEXT_STATE_THRESHOLD = 10
    SLEEP_INTERVAL = 0.1
    # NEXT_STATE_THRESHOLD = 100
    # SLEEP_INTERVAL = 0.001
    
    def __init__(self):
        self.state = self.WORK_RUN
        self.countdown_seconds = 25 * 60
        self.button_consecutive = 0
        self.point1_second = 0
        self.display = BicolorMatrix8x8.BicolorMatrix8x8(busnum=2)
        self.display.begin()
    def UpdateState(self):
        if (self.Button()):
            self.button_consecutive += 1
            if (self.button_consecutive == self.NEXT_STATE_THRESHOLD):
                if self.state < 2:
                    self.state = self.REST_RUN
                    self.countdown_seconds = 5 * 60
                    self.point1_second = 0
                else:
                    self.state = self.WORK_RUN
                    self.countdown_seconds = 25 * 60
                    self.point1_second = 0
        else:
            if (self.button_consecutive):
                if (self.button_consecutive < self.NEXT_STATE_THRESHOLD):
                    if self.state < 2:
                        self.state = 1 - self.state
                    else:
                        self.state = 5 - self.state
                self.button_consecutive = 0
        
        if (self.state == self.WORK_RUN or self.state == self.REST_RUN):
            self.point1_second += 1
            if self.point1_second == 10:
                self.point1_second = 0
                self.countdown_seconds -= 1
                
                if (self.countdown_seconds == 0):
                    if self.state == self.WORK_RUN:
                        self.state = self.REST_PAUSE
                        self.countdown_seconds = 5 * 60
                    else:
                        self.state = self.WORK_PAUSE
                        self.countdown_seconds = 25 * 60
    def GetPixel(self, x, y, num, sec):
        c = BicolorMatrix8x8.RED
        if (self.state >= 2):
            c = BicolorMatrix8x8.GREEN
        if (x == 7):
            if self.state == self.WORK_PAUSE or self.state == self.REST_PAUSE:
                return BicolorMatrix8x8.YELLOW
        if (x == 6):
            if y * 7.5 > sec:
                return 0
            else:
                return c
        if (x == 5 and y == 7):
            if self.state == self.WORK_PAUSE or self.state == self.REST_PAUSE:
                return 0
            if self.point1_second < 5:
                return c
            else:
                return 0
        if (x >= 5):
            return 0
        if y < 3:
            digit = digits[num % 10][x]
            return c if (digit >> y) & 1 else 0
        elif y >= 4 and y <= 6:
            digit = digits[num / 10][x]
            return c if (digit >> (y - 4) ) & 1 else 0
        else:
            return 0
    def Display(self):
        minute = int(math.ceil(self.countdown_seconds/60.0))
        seconds = minute * 60  - self.countdown_seconds
        print(self.state, minute, seconds)

        self.display.clear()

        for x in range(8):
            for y in range(8):
                c = self.GetPixel(x, y, minute, seconds)
                self.display.set_pixel(x, y, c)
        self.display.write_display()

    def Button(self):
        return GPIO.input("P9_12")
    
    def Run(self):
        while True:
            starttime = time.time()
            self.UpdateState();
            self.Display();
            sleeptime = self.SLEEP_INTERVAL - (time.time() - starttime)
            if sleeptime > 0:
                time.sleep(sleeptime)

def main():
    pomo = Pomo()
    pomo.Run()

if __name__ == "__main__":
    main()
