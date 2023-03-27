import RPi.GPIO as GPIO
import time

class ButtonDetector:
    def __init__(self, pin, callback):
        self.pin = pin
        self.callback = callback
        self.button_pressed = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self._button_pressed, bouncetime=300)
        
    def _button_pressed(self, channel):
        if not self.button_pressed:
            self.button_pressed = True
            self.callback(self.pin, self.is_button_pressed)
            while GPIO.input(channel) == GPIO.HIGH:
                time.sleep(0.01)
            self.button_pressed = False
        
    def cleanup(self):
        GPIO.cleanup(self.pin)

    def is_button_pressed(self):
        return self.button_pressed
