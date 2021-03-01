# how to install dependencies

## for beaglebone black

https://github.com/adafruit/adafruit-beaglebone-io-python

## for raspberry pi

Follow this link to setup I2C https://diyprojects.io/activate-i2c-bus-raspberry-pi-3-zero/#.XwodUXHYq3B

Follow this link to setup GPIO https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/


## for both beaglebone black and raspberry pi

https://github.com/adafruit/Adafruit_Python_LED_Backpack

If you see error complaining setuptools-3.5.1.zip is corrupted, you can download the file manually from 
```
wget https://files.pythonhosted.org/packages/6f/6f/c26e40e5ffa9aa4601d9fa27a7238ef38bf15d19e683a5edb2524cf156ab/setuptools-3.5.1.zip
```

For other errors, try to see if below commands can fix them
```
sudo apt-get install python-pip
sudo pip install s3cmd
sudo python -m pip install --upgrade pip setuptools wheel
```
