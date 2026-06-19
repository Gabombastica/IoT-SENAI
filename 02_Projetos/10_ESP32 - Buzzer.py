import time
from machine import Pin, PWM

PINO_BUZZER = 15
buzzer = PWM(Pin(PINO_BUZZER))
# Notas musicais (frequências em Hz) para o assobio de Kill Bill
E5 = 659
G5 = 784
A5 = 880
B5 = 988
C5 = 523
# Sequência contínua (sem pausas no meio)
melodia = [
E5, G5, A5, B5, G5, A5, B5, E5,
E5, G5, A5, B5, C5, B5, A5, B5
]

# Duração de cada nota em segundos (ajustada para manter o ritmo sem as pausas)
duracoes = [
0.45, 0.45, 0.45, 0.55, 0.22, 0.22, 0.45, 0.70,
0.45, 0.45, 0.45, 0.55, 0.22, 0.22, 0.45, 0.70
]

def tocar_nota_continua(frequencia, duracao):
    buzzer.freq(frequencia)
    buzzer.duty(512) # Mantém o som ativo (50% de duty cycle)
    time.sleep(duracao)
    
while True:
    # Não há comando buzzer.duty(0) aqui, o som emenda direto na próxima nota
    print("Tocando o assobio de Kill Bill em loop contínuo...")
    try:
        while True:
            for i in range(len(melodia)):
                tocar_nota_continua(melodia[i], duracoes[i])
    # O loop reinicia imediatamente a primeira nota, eliminando o intervalo final
    except KeyboardInterrupt:
        buzzer.deinit() # Desliga o PWM ao encerrar com Ctrl+C
        print("\nPrograma interrompido.")
