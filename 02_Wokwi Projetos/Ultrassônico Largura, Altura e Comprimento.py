# Ultrassônico para medir Largura, Altura e Comprimento

# Realizar cálculos Área da base (largura × comprimento) e Volume (altura × área da base)
# importar bibliotecas
# quem sera utilizado
#import machine # machine.Pin
from machine import Pin, ADC,time_pulse_us,I2C, SoftI2C
from hcsr04 import HCSR04
from i2c_lcd import I2cLcd
from time import sleep,ticks_ms,ticks_diff
from nec import NEC_16

# configuracao
# onde estao os itens/componentes
TRIG = Pin(13)
ECHO = Pin(12)
ultrasonico = HCSR04(trigger_pin=TRIG, echo_pin=ECHO)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000) 
lcd = I2cLcd(i2c, 0x27, 2, 16)
opcao = ""
ligado = 0

# programa
# o que / como ira acontecer
altura = 0
comprimento = 0
largura = 0
area = 0
distancia = 0
ir_data = 0

global valor_data

def callback(data, addr, ctrl):
    global ir_data
    if data >0:
        #print(f"Num_botao {data:02x} cod {addr:04x} ft {ir_key[data]}")
        print(f"Num_botao {data:02x} cod {data}")
        ir_data = data
   
        
ir = NEC_16(Pin(34, Pin.IN),callback)

# programa
# o que / como ira acontecer
while True:
  sleep(0.2)
  print(ligado)
  if ir_data > 0:
    if ir_data == 64 and ligado == 0:
      ligado = 1
      lcd.move_to(0,0)
      lcd.putstr("Ligando...")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[1] - Medir altura")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[2] - Medir comprimento")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[3] - Medir largura")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[4] - Calcular area")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[5] - Calcular volume")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("[Asterisco] - Mostrar menu")
      sleep(2)
      lcd.clear()
      sleep(0.1)
      lcd.move_to(0,0)
      lcd.putstr("[Hashtag] - Medir a distancia")
      sleep(2)
      lcd.clear()
      lcd.move_to(0,0)
      lcd.putstr("Medir tudo para calcular")
      sleep(2)
      lcd.clear()
      sleep(0.1)
      lcd.move_to(0,0)
      lcd.putstr("Medir area antes do volume")
      sleep(2)
      lcd.clear()
      sleep(0.1)
      lcd.move_to(0,0)
      lcd.putstr("Medir a distancia antes de tudo")
      sleep(2)
      lcd.clear()
    elif ir_data == 64 and ligado == 1:
      ligado = 0
      lcd.move_to(0,0)
      lcd.putstr("Desligando...")
      sleep(2)
      lcd.clear()
      ir_data = 0
    if ligado == 1:
      if ir_data > 0:
        if ir_data == 25:
          cm = ultrasonico.distance_cm()
          comprimento = distancia - cm
          lcd.move_to(0,0)
          lcd.putstr(f"Comp: {round(comprimento, 2)} cm")
          sleep(1)
          lcd.clear()
          print("Tecla 2")
          sleep(0.1)
        elif ir_data == 24:
          cm = ultrasonico.distance_cm()
          volume = altura * area
          lcd.move_to(0,0)
          lcd.putstr(f"Vol: {round(volume, 2)} cm")
          sleep(1)
          lcd.clear()
          print("Tecla 5")
          sleep(0.1)
        elif ir_data == 22:
          cm = ultrasonico.distance_cm()
          altura = distancia - cm
          lcd.move_to(0,0)
          lcd.putstr(f"Alt: {round(altura, 2)} cm")
          sleep(1)
          lcd.clear()
          print("Tecla 1")
          sleep(0.1)
        elif ir_data == 13:
          cm = ultrasonico.distance_cm()
          largura = distancia - cm
          lcd.move_to(0,0)
          lcd.putstr(f"Larg: {round(largura, 2)} cm")
          sleep(1)
          lcd.clear()
          print("Tecla 3")
          sleep(0.1)
        elif ir_data == 12:
          cm = ultrasonico.distance_cm()
          area = largura * comprimento
          lcd.move_to(0,0)
          lcd.putstr(f"Area: {round(area, 2)} cm")
          sleep(1)
          lcd.clear()
          print("Tecla 4")
          sleep(0.1)
        elif ir_data == 66:
          print("Tecla Menu")
          lcd.move_to(0,0)
          lcd.putstr("[Asterisco] - Mostrar menu")
          sleep(1)
          lcd.clear()
          sleep(0.1)
          lcd.move_to(0,0)
          lcd.putstr("[1] - Medir altura")
          sleep(2)
          lcd.clear()
          lcd.move_to(0,0)
          lcd.putstr("[2] - Medir comprimento")
          sleep(2)
          lcd.clear()
          lcd.move_to(0,0)
          lcd.putstr("[3] - Medir largura")
          sleep(2)
          lcd.clear()
          lcd.move_to(0,0)
          lcd.putstr("[4] - Calcular area")
          sleep(2)
          lcd.clear()
          lcd.move_to(0,0)
          lcd.putstr("[5] - Calcular volume")
          sleep(2)
          lcd.clear()
          sleep(0.1)
          lcd.move_to(0,0)
          lcd.putstr("[Asterisco] - Mostrar menu")
          sleep(2)
          lcd.clear()
          sleep(0.1)
          lcd.move_to(0,0)
          lcd.putstr("[Hashtag] - Medir a distancia")
          sleep(2)
          lcd.clear()
          lcd.move_to(0,0)
          lcd.putstr("Medir tudo para calcular")
          sleep(2)
          lcd.clear()
          sleep(0.1)
          lcd.move_to(0,0)
          lcd.putstr("Medir area antes do volume")
          sleep(2)
          lcd.clear()
          sleep(0.1)
          lcd.move_to(0,0)
          lcd.putstr("Medir a distancia antes de tudo")
          sleep(2)
          lcd.clear()
          sleep(0.1)
        elif ir_data == 74:
            distancia = ultrasonico.distance_cm()
            lcd.move_to(0,0)
            lcd.putstr(f"Dist: {round(distancia, 2)} cm")
            sleep(1)
            lcd.clear()
            sleep(0.1)
        else:
          lcd.move_to(0,0)
          lcd.putstr("Botao nao utilizavel")
          sleep(1)
          lcd.clear()
        ir_data = 0
      ir_data = 0
    ir_data = 0  

