from machine import Pin, ADC, PWM
import time

# ==========================================
# 1. CONFIGURAÇÃO DO HARDWARE BRUTO
# ==========================================
# Pino 34 é um pino exclusivo de entrada analógica (ADC)
sensor_cru = ADC(Pin(35))
sensor_cru2 = ADC(Pin(34))
# Configuração do ADC
sensor_cru.atten(ADC.ATTN_11DB)  # Ajusta a atenuação para permitir leituras de 0V a 3.3V
sensor_cru.width(ADC.WIDTH_9BIT)  # Define a resolução do ADC para 10 bits (valores de 0 a 1023)
#
sensor_cru2.atten(ADC.ATTN_11DB)  # Ajusta a atenuação para permitir leituras de 0V a 3.3V
sensor_cru2.width(ADC.WIDTH_9BIT)  # Define a resolução do ADC para 10 bits (valores de 0 a 1023)
############################

##print("🔬 Circuito Raiz do TCRT5000 Iniciado!")
##print("-" * 40)

# ==== CONFIGURAÇÃO DE PINOS ====
# Ajuste conforme sua ligação no ESP32
IN1 = Pin(5, Pin.OUT)   # Entrada 1 do motor A
IN2 = Pin(18, Pin.OUT)   # Entrada 2 do motor A
ENA = PWM(Pin(19), freq=1000)  # Enable A (PWM para velocidade)

IN3 = Pin(17, Pin.OUT)   # Entrada 1 do motor B
IN4 = Pin(16, Pin.OUT)   # Entrada 2 do motor B
ENB = PWM(Pin(4), freq=1000)  # Enable A (PWM para velocidade)


IN1.value(0)
IN2.value(0)
ENA.duty(0)
IN3.value(0)
IN4.value(0)
ENB.duty(0)

# ==========================================
# 2. LOOP PRINCIPAL
# ==========================================

def motorA_frente(tork, temp=0):
    """
    Gira o motor para frente.
    speed: 0 a 1023 (0% a 100% duty cycle)
    """
    ##print("A")
    IN1.value(1)
    IN2.value(0)
    ENA.duty(tork)
    if temp > 0:
        time.sleep(temp);

def motorA_tras(tork, temp=0):
    """
    Gira o motor para frente.
    speed: 0 a 1023 (0% a 100% duty cycle)
    """
    ##print("A_t")
    IN1.value(0)
    IN2.value(1)
    ENA.duty(tork)
    if temp > 0:
        time.sleep(temp);

def motorB_frente(tork, temp=0):
    """
    Gira o motor para frente.
    speed: 0 a 1023 (0% a 100% duty cycle)
    """
    ##print("B")
    IN3.value(0)
    IN4.value(1)
    ENB.duty(tork)
   
    if temp > 0:
        time.sleep(temp);
def motorB_tras(tork, temp=0):
    """
    Gira o motor para frente.
    speed: 0 a 1023 (0% a 100% duty cycle)
    """
    ##print("B")
    IN3.value(1)
    IN4.value(0)
    ENB.duty(tork)
   
    if temp > 0:
        time.sleep(temp);

def robo_frente(tork, temp=0):
    """
    Gira o motor para frente.
    speed: 0 a 1023 (0% a 100% duty cycle)
    """
    IN3.value(0)
    IN4.value(1)
    ENB.duty(tork )
    IN1.value(1)
    IN2.value(0)
    ENA.duty(tork +30)
    if temp > 0:
        time.sleep(temp);
def robo_para(temp):
    IN3.value(1)
    IN4.value(1)
    ENB.duty(400 )
    IN1.value(1)
    IN2.value(1)
    ENA.duty(400 +30)
    if temp > 0:
        time.sleep(temp);
   


while 0:
    ###print("hOhh")
    robo_frente(600,0.1)
    # Suspiro do sistema
    time.sleep_ms(100)
   

VEL = 600

while True:
    # Lê a voltagem real do "Divisor de Tensão" que você montou na protoboard
    v_1 = sensor_cru.read()
    v_2 = sensor_cru2.read()
   
    # Imprime o gráfico em tempo real para ajudar na sua calibração
   
    if v_1 > 100 and v_2 > 180:
        robo_frente(VEL,0.1)
        robo_para(0.075)
       
        msg = "L"
    elif v_1 > v_2 and v_1 > 100:
        #motorA_tras(VEL-150,0.05)
        motorB_frente(VEL-150,0.08)
        robo_para(0.075)
        msg ="e_x"
    elif v_1 > v_2:
        motorB_frente(VEL-100,0.075)
        robo_para(0.075)
        msg="e_L"
    elif v_1 < v_2 and v_2 > 170:
        #motorB_tras(VEL-150,0.05)
        motorA_frente(VEL-150,0.080)
        robo_para(0.075)
        msg="d_X"
    elif v_1 < v_2:
        motorA_frente(VEL-150,0.075)
        robo_para(0.075)
        msg="d_L"
   
    else:
        msg="S"
        print(f"[{v_1:04d}::{v_2:04d}]::{msg}")
        robo_para(5)
       
    #print(f"[{v_1:04d}::{v_2:04d}]::{msg}")
   
   
    # Suspiro do sistema
    time.sleep_ms(100)