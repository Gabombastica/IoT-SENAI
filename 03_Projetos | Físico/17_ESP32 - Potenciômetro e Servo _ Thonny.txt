# Potenciômetro para mexer o Servo
from machine import Pin, ADC, PWM
import time

servo = PWM(Pin(22, Pin.OUT), 50)

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

while True:
    estado_pot = pot.read()
    novo_valor = (estado_pot - 0) * (126 - 25) / (1023 - 0) + 25
    novo_valor = int(novo_valor)
    servo.duty(novo_valor)
    print("")
    time.sleep(0.1)
    print(f"O potenciômetro 1 tem o valor de: {novo_valor}")
