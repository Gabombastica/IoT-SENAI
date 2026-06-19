# Ultrassônico Ligar o Led (Aproximação)
from machine import Pin
from hcsr04 import HCSR04
import time

led1 = Pin(25, Pin.OUT)
led2 = Pin(33, Pin.OUT)

TRIG = Pin(12)
ECHO = Pin(13)

ultrassonico = HCSR04(trigger_pin = TRIG, echo_pin = ECHO)
var_cm = ultrassonico.distance_cm()

while True:
    var_cm = ultrassonico.distance_cm()
    print(f"CM: {var_cm}")
    if var_cm >= 40:
        led1.value(1)
        time.sleep(1)
        led1.value(0)
        time.sleep(1)
    elif var_cm >= 20 and var_cm <= 40:
        led2.value(1)
        time.sleep(0.5)
        led2.value(0)
        time.sleep(0.5)
    elif var_cm < 20:
        led2.value(1)
        time.sleep(0.1)
        led2.value(0)
        time.sleep(0.1)
        