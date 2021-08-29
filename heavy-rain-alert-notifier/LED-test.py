# Aug 28, 2021
# LED-test.py

# ref page: https://learn.adafruit.com/\
# adafruit-aw9523-gpio-expander-and-led-driver/python-circuitpython

import board
import digitalio
import adafruit_aw9523
import time

i2c = board.I2C()
aw = adafruit_aw9523.AW9523(i2c)

led_pin_G1 = aw.get_pin(1)
led_pin_G2 = aw.get_pin(2)
led_pin_G3 = aw.get_pin(3)
led_pin_G4 = aw.get_pin(4)
led_pin_G5 = aw.get_pin(5)

led_pin_Y6 = aw.get_pin(6)
led_pin_Y7 = aw.get_pin(7)
led_pin_Y12 = aw.get_pin(12)
led_pin_Y13 = aw.get_pin(13)
led_pin_Y14 = aw.get_pin(14)
led_pin_Y15 = aw.get_pin(15)
led_pin_Y0 = aw.get_pin(0)

led_pin_C11 = aw.get_pin(11)
led_pin_C10 = aw.get_pin(10)

# print(type(led_pin_G1))  # <class 'adafruit_aw9523.DigitalInOut'>

led_pins = [
    led_pin_G1, led_pin_G2,
    led_pin_G3, led_pin_G4,
    led_pin_G5,

    led_pin_Y6, led_pin_Y7,
    led_pin_Y12, led_pin_Y13,
    led_pin_Y14, led_pin_Y15,
    led_pin_Y0,

    led_pin_C11, led_pin_C10
]

for pin in led_pins:
    pin.switch_to_output(value=False)

for _ in range(10):
    for pin in led_pins:
        pin.value = True
        time.sleep(0.1)
        pin.value = False





