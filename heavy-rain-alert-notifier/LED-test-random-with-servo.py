# Aug 29, 2021
# LED-test-random-servo.py

# ref page: https://learn.adafruit.com/\
# adafruit-aw9523-gpio-expander-and-led-driver/python-circuitpython

# servo ref page:https://learn.adafruit.com/\
# adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library

import board
import digitalio
import adafruit_aw9523
import time
import random
import sys
from adafruit_servokit import ServoKit

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

#print(type(led_pin_G1))  # <class 'adafruit_aw9523.DigitalInOut'>

rain_pins = [
    led_pin_G1, led_pin_G2,
    led_pin_G3, led_pin_G4,
    led_pin_G5,

    led_pin_Y6, led_pin_Y7,
    led_pin_Y12, led_pin_Y13,
    led_pin_Y14, led_pin_Y15,
    led_pin_Y0,
]

cloud_pins = [led_pin_C11, led_pin_C10]

# set pins to output, value to False
for pin in rain_pins:
    pin.switch_to_output(value=False)

for pin in cloud_pins:
    pin.switch_to_output(value=False)


sys.exit()  # to off LEDs if it is kept on after ctrl + C



# servo
kit = ServoKit(channels=16)
kit.servo[15].actuation_range = 135
# tested on my SG-5010, 0 and 180 to see actual turn degree.
# max looks 135 degrees.

# umbrella opening: 60 looks nice.

# loop
sw_a = False
sw_b = False
turn_a = 0
turn_b = 0

# umbrella
u_open = False
turn_u = 0
while True:
    if turn_a == 0:
        sw_a = not sw_a
        turn_a = random.randint(1, 10)
        led_pin_C11.value = sw_a

    if turn_b == 0:
        sw_b = not sw_b
        turn_b = random.randint(1, 10)
        led_pin_C10.value = sw_b

    if turn_u == 0:
        u_open = not u_open
        turn_u = random.randint(20, 50)
        if u_open:
            kit.servo[15].angle = 60
            print('[debug] umbrella opened, cycle =', turn_u)
        else:
            kit.servo[15].angle = 0
            print('[debug] unbrella closed, cycle =', turn_u)

    # shuffle pin list
    random.shuffle(rain_pins)

    # select 3
    upto = random.randint(0, 2)
    if upto == 0:
        time.sleep(random.uniform(0.2, 1))
        continue

    selected = rain_pins[:upto]

    # on
    for pin in selected:
        pin.value = True
        time.sleep(random.uniform(0.05, 0.2))

    # off
    random.shuffle(selected)
    for pin in selected:
        pin.value = False
        time.sleep(random.uniform(0.05, 0.2))

    # decrement turn_a and turn_b
    turn_a -= 1
    turn_b -= 1
    turn_u -= 1
