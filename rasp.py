import RPi.GPIO as GPIO
import lib

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
 # set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.IN)

class RaspPomo(lib.Pomo):
    def Button(self):
        return GPIO.input(11)

    busnum = 1

def main():
    pomo = RaspPomo()
    pomo.Run()

if __name__ == "__main__":
    main()
