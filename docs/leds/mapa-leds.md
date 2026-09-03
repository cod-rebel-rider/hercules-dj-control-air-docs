# Mapa de LEDs — Hercules DJ Control AIR

## Objetivo

Documentar os comandos MIDI utilizados para controlar os LEDs da **Hercules DJ Control AIR**, separando claramente:

* informações oficiais da Hercules;
* comandos encontrados na implementação do Mixxx;
* resultados de testes realizados diretamente no hardware;
* inferências;
* comportamentos ainda não confirmados.

Este documento deve ser atualizado conforme novos testes forem realizados.

---

## Convenções

### Canal MIDI

A documentação oficial utiliza a notação:

```text
9x
Bx
```

onde `x` representa o canal MIDI.

Na unidade física testada neste projeto, o canal utilizado é:

```text
MIDI Channel 2
```

No protocolo MIDI isso corresponde a:

```text
Note On       → 91
Control Change → B1
```

No Mido, o canal 2 é representado pelo índice:

```python
channel=1
```

---

## Valores dos LEDs

Para mensagens `Note On`:

```text
7F = ON
00 = OFF
```

Exemplo:

```text
91 12 7F
```

Liga o LED associado ao endereço `12`.

```text
91 12 00
```

Desliga o mesmo LED.

---

## Status das informações

| Status        | Significado                                       |
| ------------- | ------------------------------------------------- |
| OFICIAL       | Informação encontrada na documentação da Hercules |
| IMPLEMENTAÇÃO | Informação encontrada em software, como Mixxx     |
| EXPERIMENTAL  | Confirmado diretamente no hardware                |
| INFERÊNCIA    | Conclusão baseada em evidências                   |
| DESCONHECIDO  | Ainda não confirmado                              |

---

# LEDs do Deck A

| Função       | Endereço | ON         | OFF        | Fonte            | Status         |
| ------------ | -------: | ---------- | ---------- | ---------------- | -------------- |
| Effect Pad 1 |     `01` | `91 01 7F` | `91 01 00` | Hercules / Mixxx | OFICIAL        |
| Effect Pad 2 |     `02` | `91 02 7F` | `91 02 00` | Hercules / Mixxx | OFICIAL        |
| Effect Pad 3 |     `03` | `91 03 7F` | `91 03 00` | Hercules / Mixxx | OFICIAL        |
| Effect Pad 4 |     `04` | `91 04 7F` | `91 04 00` | Hercules / Mixxx | OFICIAL        |
| Sample Pad 1 |     `05` | `91 05 7F` | `91 05 00` | Hercules / Mixxx | OFICIAL        |
| Sample Pad 2 |     `06` | `91 06 7F` | `91 06 00` | Hercules / Mixxx | OFICIAL        |
| Sample Pad 3 |     `07` | `91 07 7F` | `91 07 00` | Hercules / Mixxx | OFICIAL        |
| Sample Pad 4 |     `08` | `91 08 7F` | `91 08 00` | Hercules / Mixxx | OFICIAL        |
| Loop Pad 1   |     `09` | `91 09 7F` | `91 09 00` | Hercules / Mixxx | OFICIAL        |
| Loop Pad 2   |     `0A` | `91 0A 7F` | `91 0A 00` | Hercules / Mixxx | OFICIAL        |
| Loop Pad 3   |     `0B` | `91 0B 7F` | `91 0B 00` | Hercules / Mixxx | OFICIAL        |
| Loop Pad 4   |     `0C` | `91 0C 7F` | `91 0C 00` | Hercules / Mixxx | OFICIAL        |
| Sync         |     `13` | `91 13 7F` | `91 13 00` | Hercules / Mixxx | OFICIAL        |
| Cue          |     `11` | `91 11 7F` | `91 11 00` | Hercules / Mixxx | OFICIAL        |
| Play/Pause   |     `12` | `91 12 7F` | `91 12 00` | Hercules / Mixxx | **CONFIRMADO** |

### Evidência experimental

O LED Play/Pause do Deck A foi testado diretamente na unidade física.

Comando:

```text
91 12 7F
```

Resultado:

```text
LED Play/Pause Deck A → ACENDEU
```

Comando:

```text
91 12 00
```

Resultado:

```text
LED Play/Pause Deck A → APAGOU
```

**Status: EXPERIMENTAL CONFIRMADO**

---

# LEDs do Deck B

| Função       | Endereço | ON         | OFF        | Fonte            | Status  |
| ------------ | -------: | ---------- | ---------- | ---------------- | ------- |
| Effect Pad 1 |     `17` | `91 17 7F` | `91 17 00` | Hercules / Mixxx | OFICIAL |
| Effect Pad 2 |     `18` | `91 18 7F` | `91 18 00` | Hercules / Mixxx | OFICIAL |
| Effect Pad 3 |     `19` | `91 19 7F` | `91 19 00` | Hercules / Mixxx | OFICIAL |
| Effect Pad 4 |     `1A` | `91 1A 7F` | `91 1A 00` | Hercules / Mixxx | OFICIAL |
| Sample Pad 1 |     `1B` | `91 1B 7F` | `91 1B 00` | Hercules / Mixxx | OFICIAL |
| Sample Pad 2 |     `1C` | `91 1C 7F` | `91 1C 00` | Hercules / Mixxx | OFICIAL |
| Sample Pad 3 |     `1D` | `91 1D 7F` | `91 1D 00` | Hercules / Mixxx | OFICIAL |
| Sample Pad 4 |     `1E` | `91 1E 7F` | `91 1E 00` | Hercules / Mixxx | OFICIAL |
| Loop Pad 1   |     `1F` | `91 1F 7F` | `91 1F 00` | Hercules / Mixxx | OFICIAL |
| Loop Pad 2   |     `20` | `91 20 7F` | `91 20 00` | Hercules / Mixxx | OFICIAL |
| Loop Pad 3   |     `21` | `91 21 7F` | `91 21 00` | Hercules / Mixxx | OFICIAL |
| Loop Pad 4   |     `22` | `91 22 7F` | `91 22 00` | Hercules / Mixxx | OFICIAL |
| Sync         |     `29` | `91 29 7F` | `91 29 00` | Hercules / Mixxx | OFICIAL |
| Cue          |     `27` | `91 27 7F` | `91 27 00` | Hercules / Mixxx | OFICIAL |
| Play/Pause   |     `28` | `91 28 7F` | `91 28 00` | Hercules / Mixxx | OFICIAL |

---

# LEDs do Mixer / Navegação

| Função   | Endereço | ON         | OFF        | Fonte    | Status  |
| -------- | -------: | ---------- | ---------- | -------- | ------- |
| Files    |     `35` | `91 35 7F` | `91 35 00` | Hercules | OFICIAL |
| Folders  |     `36` | `91 36 7F` | `91 36 00` | Hercules | OFICIAL |
| Scratch  |     `2D` | `91 2D 7F` | `91 2D 00` | Hercules | OFICIAL |
| Magic    |     `2E` | `91 2E 7F` | `91 2E 00` | Hercules | OFICIAL |
| Record   |     `30` | `91 30 7F` | `91 30 00` | Hercules | OFICIAL |
| Listen A |     `14` | `91 14 7F` | `91 14 00` | Hercules | OFICIAL |
| Listen B |     `2A` | `91 2A 7F` | `91 2A 00` | Hercules | OFICIAL |

---

# LEDs Beat

## Deck A

| Beat LED | Endereço | ON         | OFF        | Status  |
| -------- | -------: | ---------- | ---------- | ------- |
| Beat 1   |     `44` | `91 44 7F` | `91 44 00` | OFICIAL |
| Beat 2   |     `45` | `91 45 7F` | `91 45 00` | OFICIAL |
| Beat 3   |     `46` | `91 46 7F` | `91 46 00` | OFICIAL |
| Beat 4   |     `47` | `91 47 7F` | `91 47 00` | OFICIAL |

## Deck B

| Beat LED | Endereço | ON         | OFF        | Status  |
| -------- | -------: | ---------- | ---------- | ------- |
| Beat 1   |     `4C` | `91 4C 7F` | `91 4C 00` | OFICIAL |
| Beat 2   |     `4D` | `91 4D 7F` | `91 4D 00` | OFICIAL |
| Beat 3   |     `4E` | `91 4E 7F` | `91 4E 00` | OFICIAL |
| Beat 4   |     `4F` | `91 4F 7F` | `91 4F 00` | OFICIAL |

---

# LEDs do painel frontal

| Função              | Endereço | ON         | OFF        | Fonte    | Status  |
| ------------------- | -------: | ---------- | ---------- | -------- | ------- |
| Mix Headphones      |     `39` | `91 39 7F` | `91 39 00` | Hercules | OFICIAL |
| Cue/PFL Headphones  |     `3A` | `91 3A 7F` | `91 3A 00` | Hercules | OFICIAL |
| Headphones Volume - |     `3B` | `91 3B 7F` | `91 3B 00` | Hercules | OFICIAL |
| Headphones Volume + |     `3C` | `91 3C 7F` | `91 3C 00` | Hercules | OFICIAL |

---

# Comando global

A documentação da Hercules também descreve um comando global utilizando Control Change.

Estrutura:

```text
Bx 7F valor
```

Para a unidade testada:

```text
B1 7F 00
```

Interpretação:

```text
Todos os LEDs OFF
```

E:

```text
B1 7F 7F
```

Interpretação:

```text
Todos os LEDs ON
```

## Estado experimental

O comando foi inicialmente testado utilizando o canal MIDI incorreto (`B0`) e não produziu alteração observável.

Após a descoberta de que a unidade utiliza o MIDI Channel 2, o teste correto passou a ser:

```text
B1 7F 00
B1 7F 7F
```

**Ainda não confirmado fisicamente.**

Status:

```text
EXPERIMENTAL / PENDENTE
```

---

# Tabela de validação experimental

A tabela abaixo registra somente testes realizados diretamente no hardware.

| Endereço | Função            | Comando ON | Resultado   | Status         |
| -------- | ----------------- | ---------- | ----------- | -------------- |
| `12`     | Play/Pause Deck A | `91 12 7F` | LED acendeu | **CONFIRMADO** |

---

# Testes realizados

## TEST-LED-001 — Play/Pause Deck A

### Objetivo

Confirmar se o endereço `12` controla fisicamente o LED Play/Pause do Deck A.

### Comando ON

```text
91 12 7F
```

### Resultado

LED Play/Pause Deck A acendeu.

### Comando OFF

```text
91 12 00
```

### Resultado

LED Play/Pause Deck A apagou.

### Conclusão

O endereço `12` foi confirmado na unidade física.

**Status: PASS**

---

## TEST-LED-002 — Todos os LEDs

### Objetivo

Verificar o comando global de controle dos LEDs.

### Comando OFF

```text
B1 7F 00
```

### Comando ON

```text
B1 7F 7F
```

### Resultado

Ainda não registrado.

**Status: PENDENTE**

---

# Diferença entre documentação e hardware

A documentação oficial utiliza a notação genérica:

```text
9x
Bx
```

O `x` depende do canal MIDI.

A unidade física analisada neste projeto utiliza:

```text
Canal MIDI 2
```

Portanto:

```text
9x → 91
Bx → B1
```

Essa informação foi confirmada através da captura MIDI realizada diretamente na controladora.

Exemplo capturado ao pressionar PLAY A:

```text
note_on channel=1 note=18 velocity=127
```

Convertendo:

```text
channel=1 no Mido
        ↓
MIDI Channel 2

note=18 decimal
        ↓
12 hexadecimal

velocity=127
        ↓
7F hexadecimal
```

Resultado:

```text
91 12 7F
```

O mesmo comando foi posteriormente enviado pela porta MIDI OUT e confirmou o controle físico do LED.

---

# Relação com o Mixxx

O arquivo de mapping do Mixxx contém os mesmos endereços básicos utilizados pela documentação oficial, incluindo:

```text
Play A → 12
Cue A → 11
Sync A → 13

Play B → 28
Cue B → 27
Sync B → 29
```

Entretanto, este projeto considera uma informação experimental como confirmada somente após o comando ser enviado diretamente à unidade física e sua resposta ser observada.

Portanto:

```text
Mixxx
   ↓
Referência de implementação

Hercules Manual
   ↓
Referência oficial

Hardware físico
   ↓
Validação experimental
```

---

# Questões ainda em investigação

* Todos os endereços documentados respondem da mesma forma na unidade física?
* Os LEDs de Beat utilizam exatamente os endereços documentados?
* O comando global `B1 7F 7F` funciona na unidade?
* Existem LEDs não documentados?
* Existem valores intermediários diferentes de `00` e `7F`?
* Alguns LEDs possuem comportamento de piscar ou estados especiais?
* Existem diferenças entre o comportamento do hardware e o mapping atual do Mixxx?
* O hardware possui comandos MIDI OUT adicionais que não aparecem no manual?
* Os LEDs respondem a `Note On velocity 0` e a `Note Off` de maneira equivalente?

---

# Próximo procedimento experimental

A próxima etapa deve ser automatizar o teste dos endereços MIDI.

O objetivo é enviar sequencialmente:

```text
91 XX 7F
```

para cada endereço e registrar visualmente qual LED respondeu.

Após cada teste, enviar:

```text
91 XX 00
```

para desligá-lo antes de continuar.

Isso permitirá construir uma tabela experimental:

| Endereço | LED observado     | ON  | OFF | Observação |
| -------- | ----------------- | --- | --- | ---------- |
| `01`     | —                 | —   | —   | Pendente   |
| `02`     | —                 | —   | —   | Pendente   |
| `03`     | —                 | —   | —   | Pendente   |
| ...      | ...               | ... | ... | ...        |
| `12`     | Play/Pause Deck A | OK  | OK  | Confirmado |

---

# Fontes

## Hercules

**DJ Control AIR / DJUCED Reference Manual**

Seção:

```text
D. DJ Control AIR MIDI messages
```

O manual documenta os comandos MIDI de entrada e saída da controladora, incluindo o controle dos LEDs.

## Mixxx

Arquivo:

```text
res/controllers/Hercules DJ Control AIR.midi.xml
```

Utilizado como referência de implementação para comandos MIDI e LEDs.

---

# Histórico de validação

| Data       | Descoberta                  | Resultado          |
| ---------- | --------------------------- | ------------------ |
| 2026-09-03 | Porta MIDI IN identificada  | `DJ Control Air 0` |
| 2026-09-03 | Porta MIDI OUT identificada | `DJ Control Air 1` |
| 2026-09-03 | Canal MIDI identificado     | Canal 2            |
| 2026-09-03 | PLAY A capturado            | `91 12 7F`         |
| 2026-09-03 | CUE A capturado             | `91 11 7F`         |
| 2026-09-03 | SYNC A capturado            | `91 13 7F`         |
| 2026-09-03 | PLAY B capturado            | `91 28 7F`         |
| 2026-09-03 | CUE B capturado             | `91 27 7F`         |
| 2026-09-03 | SYNC B capturado            | `91 29 7F`         |
| 2026-09-03 | LED Play A testado          | **CONFIRMADO**     |
| 2026-09-03 | Comando global              | Pendente           |
