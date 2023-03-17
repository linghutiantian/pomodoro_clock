import RPi.GPIO as GPIO
import lib
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
 # set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.IN)

class RaspPomo(lib.Pomo):
    def Button(self):
        return GPIO.input(11)

    def Alert(self):
        for i in range(2):
            GPIO.output(self.pin2, GPIO.HIGH)
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(0.008)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(self.pin2, GPIO.LOW)
            if i == 0:
                time.sleep(0.5)

    pin = 13  # buzzer
    pin2 = 15  # viberator

    def __init__(self):
        super(RaspPomo, self).__init__()
        # set up the GPIO channels - one input and one output
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.Alert()

    busnum = 1

def main():
    pomo = RaspPomo()
    pomo.Run()

if __name__ == "__main__":
    main()
