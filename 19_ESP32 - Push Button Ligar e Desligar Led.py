# Apertar o Push Button e fazer o Led piscar
from machine import Pin
import time

led = Pin(18, Pin.OUT)
botao = Pin(19, Pin.IN, Pin.PULL_DOWN)

while True:
    estado_botao = botao.value()
    print(estado_botao)
    if estado_botao == 1:
        estado_led = led.value()
        if estado_led == 1:
            led.value(0)
            time.sleep(0.1)
        elif estado_led == 0:
            led.value(1)
            time.sleep(0.1)
    time.sleep(0.1)
    