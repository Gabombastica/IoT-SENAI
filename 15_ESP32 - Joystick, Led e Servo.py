# Joystick para ligar e desligar o Led e para controlar o Servo
from machine import Pin, ADC, PWM
import time

servo = PWM(Pin(22, Pin.OUT), 50)
led = Pin(19, Pin.OUT)

joystick = ADC(Pin(12))
joystick.atten(ADC.ATTN_11DB)
joystick.width(ADC.WIDTH_10BIT)

while True:
    estado_joystick = joystick.read()
    novo_valor = (estado_joystick - 0) * (126 - 25) / (1023 - 0) + 25
    novo_valor = int(novo_valor)
    servo.duty(novo_valor)
    print("")
    sleep(1)
    print(f"O potenciômetro 1 tem o valor de: {novo_valor}")
    
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)