# Scripts

Scripts auxiliares para investigação e teste da controladora **Hercules DJ Control AIR**.

Os scripts desta pasta são utilizados para testar diretamente a comunicação MIDI entre o computador e a controladora, sem depender do Mixxx ou de outro software de DJ.

---

## Requisitos

* Windows
* Python 3.14 ou compatível
* Hercules DJ Control AIR conectada via USB
* `mido`
* `python-rtmidi`

Instalação:

```text
py -m pip install mido python-rtmidi
```

---

## Portas MIDI

A DJ Control AIR é apresentada pelo Windows como duas portas MIDI:

| Função   | Porta              |
| -------- | ------------------ |
| MIDI IN  | `DJ Control Air 0` |
| MIDI OUT | `DJ Control Air 1` |

### MIDI IN

A porta `DJ Control Air 0` representa as mensagens enviadas pela controladora para o computador.

Exemplos:

```text
PLAY A  → 91 12 7F
CUE A   → 91 11 7F
SYNC A  → 91 13 7F
```

### MIDI OUT

A porta `DJ Control Air 1` representa as mensagens enviadas pelo computador para a controladora.

É utilizada pelos scripts de teste de LEDs.

---

## Canal MIDI

A unidade testada utiliza **MIDI Channel 2**.

No protocolo MIDI:

```text
Canal MIDI: 2
```

No Mido, os canais são representados de `0` a `15`.

Portanto:

```python
MIDI_CHANNEL = 1
```

representa:

```text
MIDI Channel 2
```

### Status bytes

Para mensagens `Note On`:

```text
91
```

Para mensagens `Control Change`:

```text
B1
```

---

# `led_test.py`

Testa individualmente os LEDs utilizando mensagens `Note On`.

## Uso

Acender um LED:

```text
py led_test.py <endereço>
```

Apagar:

```text
py led_test.py <endereço> off
```

O endereço deve ser informado em hexadecimal.

### Exemplo

Para testar o LED Play/Pause do Deck A:

```text
py led_test.py 12
```

O comando enviado será:

```text
91 12 7F
```

Para apagar:

```text
py led_test.py 12 off
```

O comando enviado será:

```text
91 12 00
```

---

## Primeiro LED confirmado

O seguinte comando foi testado fisicamente na unidade:

```text
91 12 7F
```

Resultado:

```text
LED Play/Pause Deck A → ON
```

E:

```text
91 12 00
```

Resultado:

```text
LED Play/Pause Deck A → OFF
```

### Status

**CONFIRMADO NO HARDWARE**

---

# `led_test_all.py`

Testa o comando global de LEDs documentado para a controladora.

O script primeiro envia:

```text
B1 7F 00
```

Depois de 1 segundo:

```text
B1 7F 7F
```

A interpretação documentada é:

```text
B1 7F 00 → todos os LEDs OFF
B1 7F 7F → todos os LEDs ON
```

## Uso

```text
py led_test_all.py
```

### Observação

O comando global foi corrigido para utilizar o **MIDI Channel 2**.

A resposta física deste comando ainda deve ser validada experimentalmente.

**Status: EXPERIMENTAL**

---

# Relação com o protocolo MIDI

Os scripts utilizam diretamente os comandos documentados no protocolo da DJ Control AIR.

Estrutura de uma mensagem `Note On`:

```text
91 NN VV
```

Onde:

| Campo | Significado             |
| ----- | ----------------------- |
| `91`  | Note On, MIDI Channel 2 |
| `NN`  | Número da nota/endereço |
| `VV`  | Velocidade/estado       |

Para LEDs:

```text
7F = ON
00 = OFF
```

Exemplo:

```text
91 12 7F
```

significa:

```text
Note On
Canal 2
Nota 12
Valor 7F
```

---

# Segurança dos testes

Os scripts enviam somente mensagens MIDI para a porta:

```text
DJ Control Air 1
```

Eles não modificam arquivos da controladora nem alteram permanentemente sua configuração.

Os testes podem ser interrompidos fechando o programa ou utilizando:

```text
Ctrl+C
```

---

# Classificação dos scripts

| Script            | Função                       | Classificação |
| ----------------- | ---------------------------- | ------------- |
| `led_test.py`     | Teste individual de LED      | Experimental  |
| `led_test_all.py` | Teste global de LEDs         | Experimental  |
| `midi_monitor.py` | Captura de mensagens MIDI IN | Experimental  |

---

# Evidências confirmadas

Até o momento, foi confirmado fisicamente:

```text
MIDI IN
DJ Control Air 0

MIDI OUT
DJ Control Air 1

MIDI Channel
2

LED Play/Pause Deck A
ON  → 91 12 7F
OFF → 91 12 00
```

O restante do mapa de LEDs ainda precisa ser validado individualmente.

---

# Próximos testes

1. Validar o comando global `B1 7F 7F`.
2. Testar individualmente os endereços dos LEDs.
3. Registrar a resposta física de cada endereço.
4. Comparar os resultados com:

   * documentação oficial da Hercules;
   * mapping do Mixxx;
   * comportamento observado no hardware.
5. Atualizar `docs/leds/led-map.md` com os resultados experimentais.

---

## Princípio da documentação

Os scripts não devem ser tratados como prova definitiva do protocolo.

Cada descoberta deve ser classificada como:

* **OFICIAL**: informação encontrada na documentação da Hercules.
* **IMPLEMENTAÇÃO**: comportamento encontrado em softwares como Mixxx.
* **EXPERIMENTAL**: comportamento observado diretamente no hardware.
* **INFERÊNCIA**: conclusão baseada em evidências.
* **DESCONHECIDO**: comportamento ainda não confirmado.
