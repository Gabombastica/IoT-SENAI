# Código do LCD
from machine import Pin, ADC, time_pulse_us, I2C, SoftI2C
from time import sleep, ticks_ms, ticks_diff
from i2c_lcd import I2cLcd

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, 0x27, 2, 16)

led = Pin(23,Pin.OUT)
botao = Pin(19,Pin.IN, Pin.PULL_DOWN)

while True:
    estado_botao = botao.value()
    print(f"botao = {estado_botao}")
    if estado_botao == 1:
        estado_led = led.value()
        if estado_led == 1:
            led.value(0)
            lcd.move_to(0,0)
            lcd.putstr('Luz apagou')
            sleep(1)
            lcd.clear()
        else:
            led.value(1)
            lcd.move_to(0,0)
            lcd.putstr('Luz acendeu')
            sleep(1)
            lcd.clear()
    sleep(0.1)