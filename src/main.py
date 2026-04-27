import machine
import time

# Configuração dos Pinos (Exemplo)
led_foco = machine.Pin(15, machine.Pin.OUT)
led_pausa = machine.Pin(14, machine.Pin.OUT)
botao = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# Estados da Máquina
ESTADO_OCIOSO = 0
ESTADO_FOCO = 1
ESTADO_PAUSA = 2

estado_atual = ESTADO_OCIOSO
ultimo_tempo = time.ticks_ms()
intervalo_foco = 25 * 60 * 1000 # 25 minutos em ms

def atualizar_estado():
    global estado_atual, ultimo_tempo
    tempo_atual = time.ticks_ms()
    
    # Lógica de transição não-bloqueante
    if estado_atual == ESTADO_FOCO:
        led_foco.value(1)
        led_pausa.value(0)
        # Se o tempo passou, muda para pausa
        if time.ticks_diff(tempo_atual, ultimo_tempo) >= intervalo_foco:
            estado_atual = ESTADO_PAUSA
            ultimo_tempo = tempo_atual
            
    elif estado_atual == ESTADO_PAUSA:
        # Lógica similar para a pausa...
        pass
        
    elif estado_atual == ESTADO_OCIOSO:
        # Fica aguardando o clique do botão
        pass

# Loop Principal limpo e rápido
while True:
    # 1. Lê as entradas (Debounce do botão)
    # 2. Atualiza a máquina de estados
    atualizar_estado()
    # 3. Pequeno delay apenas para não sobrecarregar a CPU (opcional, ex: sleep_ms(10))