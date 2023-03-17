import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up a callback function to be called when any GPIO pin changes
def gpio_callback(channel):
    print("GPIO pin %s changed" % channel)

# Loop through all available GPIO pins and set up event detection
for i in range(28): # GPIO 0 to GPIO 27 (pins 27 and 28 are reserved)
    if i == 17:
        continue
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(i, GPIO.BOTH, callback=gpio_callback)

# Wait for events
while True:
    pass
