# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

### 👤 Identificação do Candidato
- **Nome completo:** Paulo Gabriel Leite Landim
- **GitHub:** https://github.com/LandimPG

---

## 1️⃣ Visão Geral da Solução
O projeto desenvolvido é um **Temporizador de Foco Inteligente (Estilo Pomodoro)**. O sistema embarcado tem como objetivo auxiliar no gerenciamento de tempo e produtividade, alternando entre ciclos de trabalho e pausas. O usuário interage com o sistema por meio de um único botão (Pushbutton) que atua como controle de Início, Parada e Cancelamento, enquanto o feedback visual do estado atual é dado por três LEDs distintos.

## 2️⃣ Arquitetura do Sistema Embarcado
O fluxo principal (`main.py`) foi estruturado utilizando uma **Máquina de Estados Finita (FSM - Finite State Machine)**. A arquitetura foi desenhada para ser totalmente **não-bloqueante**, evitando o uso de `time.sleep()`.

* **Estados:** O sistema transita entre `ESTADO_OCIOSO` (Aguardando), `ESTADO_FOCO` (Trabalho) e `ESTADO_PAUSA` (Descanso).
* **Fluxo de Dados:** Um loop principal contínuo avalia duas funções a cada iteração:
    1.  `gerenciar_botao()`: Avalia as entradas do usuário.
    2.  `gerenciar_tempo()`: Avalia se o tempo do estado atual expirou.
* **Temporização:** Utiliza-se a função `time.ticks_ms()` para registrar *timestamps* e `time.ticks_diff()` para calcular o tempo decorrido, permitindo que a CPU continue processando outras instruções enquanto o tempo corre.

## 3️⃣ Componentes Utilizados na Simulação
O hardware virtual definido no `diagram.json` contém:
* **1x Raspberry Pi Pico:** Microcontrolador principal executando MicroPython.
* **3x LEDs (Vermelho, Verde, Amarelo):** Atuadores visuais indicando, respectivamente, Foco, Pausa e Ocioso.
* **3x Resistores (330Ω):** Proteção limitadora de corrente para os LEDs (Boas práticas de hardware).
* **1x Pushbutton:** Sensor de entrada digital (Start/Stop) conectado ao GP16.

## 4️⃣ Decisões Técnicas Relevantes
* **Debounce por Software:** Em vez de usar capacitores (hardware) ou interrupções complexas, implementei um debounce temporal via software (polling). Ao detectar uma borda de descida (botão pressionado), o sistema ignora novas leituras por 250ms, evitando múltiplas leituras falsas causadas pelo "quique" mecânico do botão.
* **Pull-Up Interno:** Utilizei o resistor de pull-up interno do RP2040 (`machine.Pin.PULL_UP`) no botão, simplificando o circuito externo e garantindo nível lógico alto (1) por padrão.
* **Roteamento Visual:** O diagrama no Wokwi foi organizado utilizando roteamento ortogonal, facilitando a legibilidade do esquemático.

## 5️⃣ Resultados Obtidos
O sistema cumpre integralmente os requisitos:
* A máquina de estados opera de forma fluida sem travar o processador.
* O debounce inibe acionamentos acidentais.
* A transição automática de tempo (Foco -> Pausa -> Ocioso) ocorre com precisão milimétrica na simulação do Wokwi.
* O código passa com sucesso pela pipeline de CI/CD (GitHub Actions), comprovando a sintaxe correta e a integração com a API do Wokwi.

## 6️⃣ Comentários Adicionais
**Possíveis Melhorias Futuras:**
Com mais tempo de desenvolvimento, o projeto poderia ser expandido com:
1.  **Display OLED I2C:** Para exibir a contagem regressiva visual do tempo restante.
2.  **Buzzer PWM:** Para emitir bipes sonoros ao final de cada ciclo, dispensando a necessidade de o usuário olhar para os LEDs constantemente.
3.  **IoT (Pico W):** Integração com rede Wi-Fi e protocolo MQTT para enviar métricas de tempo de foco diário para um dashboard em nuvem.