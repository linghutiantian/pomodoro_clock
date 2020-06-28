import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_12", GPIO.IN)

if GPIO.input("P9_12"):
    print("HIGH")
else:
    print("LOW")
