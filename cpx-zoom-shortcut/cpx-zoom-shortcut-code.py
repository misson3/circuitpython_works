# May16, 2021, ms
# assign keyboard shortcut to button A and B
# A: mute/unmute microphone
# B: stop/start video
# slide switch: Win <-> Mac

# Zoom/Windows
# toggle microphone: Alt + A
# toggle camera: Alt + V

# Zoom/Mac
# toggle microphone: Cmd + Shift + A
# toggle camera: Cmd + Shift + V

# ===== USAGE NOTE ======================
# mute, stop mic and cam on PC/Mac first
# to sync initial neopixel states.
# =======================================

# --- to consider --------------------
# Microsoft Teams/Windows
# toggle microphone: Ctrl + Shift + M
# toggle camera: Crtl + Shift + O

# Google Hangout/Windows
# ------------------------------------

import board
from digitalio import DigitalInOut, Direction, Pull
# import neopixel  # neopixel is initialized in adafruit_circuitplayground lib
# see: https://github.com/adafruit/circuitpython/issues/1134
import time
import usb_hid
import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_circuitplayground import cp

# cp.switch: left=True, right=False
# left: windows
# right: mac

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# colors
mic_color = fancy.CHSV(0, 1.0, 0.01).pack()  # hue, saturation, value
cam_color = fancy.CHSV(0.6, 1.0, 0.01).pack()  # hue, saturation, value

# on start upp HUE cycle
# confrict with cp.  Follow cp.
# npx = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
npx = cp.pixels

# strt up
i = 0
while i < 1:
    for pp in range(10):
        h = (pp * (1.0/10) + i) % 1.0
        hsvcolor = fancy.CHSV(h, 1.0, 0.01)  # hue, saturation, value
        npx[pp] = hsvcolor.pack()
        npx.show()
        time.sleep(0.03)
    i = i + 0.1
# off all
npx.fill((0, 0, 0))
npx.show()

# buttons: confrict with cp, follow cp's way
# btnA = DigitalInOut(board.BUTTON_A)
# btnA = DigitalInOut(board.BUTTON_A)
# btnB = DigitalInOut(board.BUTTON_B)
# btnA.direction = Direction.INPUT
# btnB.direction = Direction.INPUT
# btnA.pull = Pull.DOWN
# btnB.pull = Pull.DOWN

mic_status = False
cam_status = False


def neopix_control(idxs, rgb):
    #Anpx.brightness = 0.2
    for i in idxs:
        npx[i] = rgb
    npx.show()


while True:
    # when button pressed
    #if btnA.value:
    if cp.button_a:
        if cp.switch:  # True=Left=Windows
            kbd.send(Keycode.ALT, Keycode.A)  # --- win Zoon
        else:  # False=Right=Mac (=Teams on win)
            # kbd.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)  # --- mac
            kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)  # win Teams
        if mic_status:  # was on.  turn it off
            neopix_control([1, 2, 3], (0, 0, 0))
        else:  # was off.  turn it on
            neopix_control([1, 2, 3], mic_color)
        # toggle status
        mic_status = not mic_status
        while cp.button_a:
        #while btnA.value:
            pass
    if cp.button_b:
    #if btnB.value:
        if cp.switch:  # True=Left=Windows
            kbd.send(Keycode.ALT, Keycode.V)  # --- win Zoon
        else:  # False=Right=Mac (=Teams on win)
            # kbd.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)  # --- mac
            kbd.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.O)  # win Teams
        if cam_status:  # was on.  turn it off
            neopix_control([6, 7, 8], (0, 0, 0))
        else:  # was off.  turn it on
            neopix_control([6, 7, 8], cam_color)
        # toggle status
        cam_status = not cam_status
        while cp.button_b:
        #while btnB.value:
            pass
