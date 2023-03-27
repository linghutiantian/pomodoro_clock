from display import Display
import os
import button
import time
import threading
from encoder import Encoder
import RPi.GPIO as GPIO



class NewClock:
    SLEEP_INTERVAL = 0.1

    def __init__(self):
        self.display = Display()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.point1_seconds = 0

    def clock_thread(self):
        while True:
            starttime = time.time()
            self.display.ShowTime(minutes=self.minutes, seconds=self.seconds, point1_seconds=self.point1_seconds)
            sleeptime = self.SLEEP_INTERVAL - (time.time() - starttime)
            if sleeptime > 0:
                time.sleep(sleeptime)
            self.point1_seconds += 1
            if self.point1_seconds == 10:
                self.point1_seconds = 0
                self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
               self.minutes = 0
               self.hours += 1

    def run(self):
        thread = threading.Thread(target=self.clock_thread)
        thread.start()
	try:
            thread.join()
	except KeyboardInterrupt:
	    print('interrupted!')
            return

class Counter:
    COUNT_PATH = '/home/pi/count.txt'
    buz_pin = 27  # buzzer
    vib_pin = 22  # viberator

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.encoder = Encoder(10, 9, self.valueChanged)
        self.display = Display()

        GPIO.setup(self.buz_pin, GPIO.OUT)  # buzzer
        GPIO.setup(self.vib_pin, GPIO.OUT)  # viberator

        in_f = open(self.COUNT_PATH, 'r')
        count_str = in_f.read()
        if not count_str:
            self.count = 0
        else:
            self.count = int(count_str)
        in_f.close()


    def valueChanged(self, value, direction):
        if direction == "R":
            self.count += 1
        else:
            self.count -= 1
        print("* New value: {}, Direction: {}".format(self.count, direction))
        self.display.ShowTime(minutes=self.count, seconds=0, point1_seconds=0)
        self.buzz()
        f = open(self.COUNT_PATH, 'w+')
        f.write(str(self.count))
        f.close()


    def buzz(self):
        GPIO.output(self.vib_pin, GPIO.HIGH)
        GPIO.output(self.buz_pin, GPIO.HIGH)
        time.sleep(0.008)
        GPIO.output(self.buz_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.vib_pin, GPIO.LOW)

    def run(self):
        self.display.ShowTime(minutes=self.count, seconds=0, point1_seconds=0)

	try:
	    while True:
	        time.sleep(10)
	except KeyboardInterrupt:
	    print('interrupted!')
            return



def main():
    # clock = NewClock()
    clock = Counter()
    clock.run()


if __name__ == "__main__":
    main()
