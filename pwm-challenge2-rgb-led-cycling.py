import board
import pwmio
import keypad
import time

led = pwmio.PWMOut(board.D7, frequency=5000, duty_cycle=0)
keys = keypad.Keys((board.D8,), value_when_pressed=False, pull=True)
light_on = False
is_pressed = False
percent_bright = 0 #a method for percentage of duty cycle: int(65535 * percent_bright)

while True:
    event=keys.events.get()
    if event and event.pressed:
        is_pressed = ...
        light_on = not ...
        if ...:
            led.duty_cycle = ...
        else:
            led.duty_cycle

    if event and event.released:
        is_pressed = ...

    if is_pressed and light_on:
        percent_bright = ...
        if percent_bright > ...:
            percent_bright = 0.1
        led.duty_cycle = ...
        time.sleep(1)
