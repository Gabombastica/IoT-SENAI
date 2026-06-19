# Potenciômetro para regular a intensidade do Led
from machine import Pin, ADC, PWM
import time

pot = ADC(Pin(34))
pwm = PWM(Pin(5))

pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

while True:
    estado_pot = pot.read()
    print(f"O valor do potenciômetro é {estado_pot}")
    pwm.duty(estado_pot)
    time.sleep(0.1)