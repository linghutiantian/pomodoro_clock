import Adafruit_BBIO.GPIO as GPIO
import lib

GPIO.setup("P9_12", GPIO.IN)

class BbbPomo(lib.Pomo):
    def Button(self):
        return GPIO.input("P9_12")

    busnum = 2

def main():
    pomo = BbbPomo()
    pomo.Run()

if __name__ == "__main__":
    main()
