# Mapa de LEDs

Documentação dos LEDs e das mensagens MIDI utilizadas para controlar os indicadores luminosos do **Hercules DJ Control AIR**.

> **Status:** Em documentação
> **Fonte primária:** Hercules / DJUCED Reference Manual
> **Última revisão:** 2026-09-03

---

## 1. Objetivo

Este documento tem como objetivo identificar:

* todos os LEDs documentados no Hercules DJ Control AIR;
* o endereço MIDI associado a cada LED;
* a mensagem utilizada para ligá-lo;
* a mensagem utilizada para desligá-lo;
* o comportamento observado durante os testes;
* diferenças entre a documentação oficial e a implementação em softwares;
* possíveis comportamentos não documentados.

A documentação será construída em três etapas:

```text
DOCUMENTAÇÃO OFICIAL
        │
        ▼
MAPA MIDI TEÓRICO
        │
        ▼
TESTE NO HARDWARE
        │
        ▼
MAPA MIDI VALIDADO
```

---

# 2. Convenções

## 2.1 Mensagem MIDI

As mensagens são representadas em hexadecimal:

```text
STATUS DATA1 DATA2
```

Exemplo:

```text
90 12 7F
```

---

## 2.2 Canal MIDI

A documentação oficial utiliza:

```text
9x
Bx
```

O `x` representa o canal MIDI.

Para o canal MIDI 1:

```text
9x → 90
Bx → B0
```

Portanto, quando um teste for realizado no canal 1, a mensagem será registrada utilizando `90` ou `B0`.

---

## 2.3 Estado do LED

A documentação oficial especifica:

```text
00 = OFF
7F = ON
```

Assim:

```text
90 NN 00
```

desliga o LED associado ao endereço `NN`.

E:

```text
90 NN 7F
```

liga o LED.

---

# 3. Classificação

Cada LED terá dois tipos de informação:

### Documentação

Indica aquilo que está explicitamente especificado pela Hercules.

### Teste

Indica aquilo que foi observado diretamente no hardware.

Usaremos os seguintes estados:

| Estado           | Significado                             |
| ---------------- | --------------------------------------- |
| ⬜ Não testado    | Ainda não realizamos o teste            |
| 🟢 Confirmado    | Hardware respondeu conforme esperado    |
| 🟡 Divergente    | Hardware respondeu de maneira diferente |
| 🔴 Não respondeu | Nenhuma resposta observada              |
| 🔵 Parcial       | Funcionamento parcialmente confirmado   |

---

# 4. Deck A

## 4.1 Pads

Os pads do Deck A possuem LEDs associados às funções Effect, Sample e Loop.

### Effect

| LED            | Endereço | OFF        | ON         | Teste |
| -------------- | -------: | ---------- | ---------- | ----- |
| Pad 1 Effect A |     `01` | `90 01 00` | `90 01 7F` | ⬜     |
| Pad 2 Effect A |     `02` | `90 02 00` | `90 02 7F` | ⬜     |
| Pad 3 Effect A |     `03` | `90 03 00` | `90 03 7F` | ⬜     |
| Pad 4 Effect A |     `04` | `90 04 00` | `90 04 7F` | ⬜     |

### Sample

| LED            | Endereço | OFF        | ON         | Teste |
| -------------- | -------: | ---------- | ---------- | ----- |
| Pad 1 Sample A |     `05` | `90 05 00` | `90 05 7F` | ⬜     |
| Pad 2 Sample A |     `06` | `90 06 00` | `90 06 7F` | ⬜     |
| Pad 3 Sample A |     `07` | `90 07 00` | `90 07 7F` | ⬜     |
| Pad 4 Sample A |     `08` | `90 08 00` | `90 08 7F` | ⬜     |

### Loop

| LED          | Endereço | OFF        | ON         | Teste |
| ------------ | -------: | ---------- | ---------- | ----- |
| Pad 1 Loop A |     `09` | `90 09 00` | `90 09 7F` | ⬜     |
| Pad 2 Loop A |     `0A` | `90 0A 00` | `90 0A 7F` | ⬜     |
| Pad 3 Loop A |     `0B` | `90 0B 00` | `90 0B 7F` | ⬜     |
| Pad 4 Loop A |     `0C` | `90 0C 00` | `90 0C 7F` | ⬜     |

---

## 4.2 Reprodução

| LED    | Endereço | OFF        | ON         | Teste |
| ------ | -------: | ---------- | ---------- | ----- |
| Cue A  |     `11` | `90 11 00` | `90 11 7F` | ⬜     |
| Play A |     `12` | `90 12 00` | `90 12 7F` | ⬜     |

---

## 4.3 Pitch

| LED    | Endereço | OFF        | ON         | Teste |
| ------ | -------: | ---------- | ---------- | ----- |
| Sync A |     `13` | `90 13 00` | `90 13 7F` | ⬜     |

---

## 4.4 Monitoramento

| LED           | Endereço | OFF        | ON         | Teste |
| ------------- | -------: | ---------- | ---------- | ----- |
| Listen Deck A |     `14` | `90 14 00` | `90 14 7F` | ⬜     |

---

# 5. Deck B

## 5.1 Pads

### Effect

| LED            | Endereço | OFF        | ON         | Teste |
| -------------- | -------: | ---------- | ---------- | ----- |
| Pad 1 Effect B |     `17` | `90 17 00` | `90 17 7F` | ⬜     |
| Pad 2 Effect B |     `18` | `90 18 00` | `90 18 7F` | ⬜     |
| Pad 3 Effect B |     `19` | `90 19 00` | `90 19 7F` | ⬜     |
| Pad 4 Effect B |     `1A` | `90 1A 00` | `90 1A 7F` | ⬜     |

### Sample

| LED            | Endereço | OFF        | ON         | Teste |
| -------------- | -------: | ---------- | ---------- | ----- |
| Pad 1 Sample B |     `1B` | `90 1B 00` | `90 1B 7F` | ⬜     |
| Pad 2 Sample B |     `1C` | `90 1C 00` | `90 1C 7F` | ⬜     |
| Pad 3 Sample B |     `1D` | `90 1D 00` | `90 1D 7F` | ⬜     |
| Pad 4 Sample B |     `1E` | `90 1E 00` | `90 1E 7F` | ⬜     |

### Loop

| LED          | Endereço | OFF        | ON         | Teste |
| ------------ | -------: | ---------- | ---------- | ----- |
| Pad 1 Loop B |     `1F` | `90 1F 00` | `90 1F 7F` | ⬜     |
| Pad 2 Loop B |     `20` | `90 20 00` | `90 20 7F` | ⬜     |
| Pad 3 Loop B |     `21` | `90 21 00` | `90 21 7F` | ⬜     |
| Pad 4 Loop B |     `22` | `90 22 00` | `90 22 7F` | ⬜     |

---

## 5.2 Reprodução

| LED    | Endereço | OFF        | ON         | Teste |
| ------ | -------: | ---------- | ---------- | ----- |
| Cue B  |     `27` | `90 27 00` | `90 27 7F` | ⬜     |
| Play B |     `28` | `90 28 00` | `90 28 7F` | ⬜     |

---

## 5.3 Pitch

| LED    | Endereço | OFF        | ON         | Teste |
| ------ | -------: | ---------- | ---------- | ----- |
| Sync B |     `29` | `90 29 00` | `90 29 7F` | ⬜     |

---

## 5.4 Monitoramento

| LED           | Endereço | OFF        | ON         | Teste |
| ------------- | -------: | ---------- | ---------- | ----- |
| Listen Deck B |     `2A` | `90 2A 00` | `90 2A 7F` | ⬜     |

---

# 6. LEDs centrais

A Hercules documenta três LEDs associados aos controles centrais.

| LED     | Endereço | OFF        | ON         | Teste |
| ------- | -------: | ---------- | ---------- | ----- |
| Scratch |     `2D` | `90 2D 00` | `90 2D 7F` | ⬜     |
| Magic   |     `2E` | `90 2E 00` | `90 2E 7F` | ⬜     |
| Record  |     `30` | `90 30 00` | `90 30 7F` | ⬜     |

---

# 7. LEDs do navegador

O controlador possui LEDs associados aos controles do navegador.

| LED     | Endereço | OFF        | ON         | Teste |
| ------- | -------: | ---------- | ---------- | ----- |
| Files   |     `35` | `90 35 00` | `90 35 7F` | ⬜     |
| Folders |     `36` | `90 36 00` | `90 36 7F` | ⬜     |

---

# 8. VU-meter de batidas

O DJ Control AIR possui indicadores luminosos utilizados como **Beat VU-Meter**.

A documentação identifica quatro LEDs para cada deck.

## 8.1 Deck A

| LED      | Endereço | OFF        | ON         | Teste |
| -------- | -------: | ---------- | ---------- | ----- |
| Beat 1 A |     `44` | `90 44 00` | `90 44 7F` | ⬜     |
| Beat 2 A |     `45` | `90 45 00` | `90 45 7F` | ⬜     |
| Beat 3 A |     `46` | `90 46 00` | `90 46 7F` | ⬜     |
| Beat 4 A |     `47` | `90 47 00` | `90 47 7F` | ⬜     |

## 8.2 Deck B

| LED      | Endereço | OFF        | ON         | Teste |
| -------- | -------: | ---------- | ---------- | ----- |
| Beat 1 B |     `4C` | `90 4C 00` | `90 4C 7F` | ⬜     |
| Beat 2 B |     `4D` | `90 4D 00` | `90 4D 7F` | ⬜     |
| Beat 3 B |     `4E` | `90 4E 00` | `90 4E 7F` | ⬜     |
| Beat 4 B |     `4F` | `90 4F 00` | `90 4F 7F` | ⬜     |

---

# 9. Painel frontal

Os controles do painel frontal possuem LEDs controláveis por MIDI.

| LED                   | Endereço | OFF        | ON         | Teste |
| --------------------- | -------: | ---------- | ---------- | ----- |
| Mix in Headphones     |     `39` | `90 39 00` | `90 39 7F` | ⬜     |
| Cue/PFL in Headphones |     `3A` | `90 3A 00` | `90 3A 7F` | ⬜     |
| Headphones Volume -   |     `3B` | `90 3B 00` | `90 3B 7F` | ⬜     |
| Headphones Volume +   |     `3C` | `90 3C 00` | `90 3C 7F` | ⬜     |

---

# 10. Resumo dos LEDs

| Grupo                 | Quantidade |
| --------------------- | ---------: |
| Pads Deck A           |         12 |
| Reprodução Deck A     |          2 |
| Sync Deck A           |          1 |
| Listen Deck A         |          1 |
| Pads Deck B           |         12 |
| Reprodução Deck B     |          2 |
| Sync Deck B           |          1 |
| Listen Deck B         |          1 |
| Controles centrais    |          3 |
| Navegador             |          2 |
| Beat VU-meter Deck A  |          4 |
| Beat VU-meter Deck B  |          4 |
| Painel frontal        |          4 |
| **Total documentado** |     **49** |

> O total acima representa os **endereços/indicadores documentados pela Hercules**, não necessariamente 49 LEDs físicos independentes. Alguns elementos físicos podem possuir múltiplas funções ou modos de iluminação.

---

# 11. Comando para atualizar todos os LEDs

A Hercules também documenta uma mensagem especial para controlar todos os LEDs simultaneamente.

Formato:

```text
Bx 7F Value
```

Valores:

| Valor | Resultado         |
| ----: | ----------------- |
|  `00` | Todos os LEDs OFF |
|  `7F` | Todos os LEDs ON  |

No canal MIDI 1:

### Desligar todos

```text
B0 7F 00
```

### Ligar todos

```text
B0 7F 7F
```

Este comando deverá ser um dos primeiros testes realizados no hardware.

---

# 12. Teste de LED individual

Para testar um LED individual no canal MIDI 1:

### 1. Desligar

Enviar:

```text
90 NN 00
```

### 2. Ligar

Enviar:

```text
90 NN 7F
```

Onde:

```text
NN = endereço do LED
```

### Exemplo: Play Deck A

Desligar:

```text
90 12 00
```

Ligar:

```text
90 12 7F
```

---

# 13. Teste de todos os LEDs

O teste global deve seguir esta sequência:

```text
B0 7F 00
```

Resultado esperado:

```text
Todos os LEDs apagados
```

Depois:

```text
B0 7F 7F
```

Resultado esperado:

```text
Todos os LEDs acesos
```

Se o resultado observado for diferente, registrar no relatório experimental.

---

# 14. Matriz de validação

Esta seção será preenchida durante os testes físicos.

| Endereço | LED esperado        | Resposta física | Estado | Observação |
| -------: | ------------------- | --------------- | ------ | ---------- |
|     `01` | Pad 1 Effect A      | —               | ⬜      |            |
|     `02` | Pad 2 Effect A      | —               | ⬜      |            |
|     `03` | Pad 3 Effect A      | —               | ⬜      |            |
|     `04` | Pad 4 Effect A      | —               | ⬜      |            |
|     `05` | Pad 1 Sample A      | —               | ⬜      |            |
|     `06` | Pad 2 Sample A      | —               | ⬜      |            |
|     `07` | Pad 3 Sample A      | —               | ⬜      |            |
|     `08` | Pad 4 Sample A      | —               | ⬜      |            |
|     `09` | Pad 1 Loop A        | —               | ⬜      |            |
|     `0A` | Pad 2 Loop A        | —               | ⬜      |            |
|     `0B` | Pad 3 Loop A        | —               | ⬜      |            |
|     `0C` | Pad 4 Loop A        | —               | ⬜      |            |
|     `11` | Cue A               | —               | ⬜      |            |
|     `12` | Play A              | —               | ⬜      |            |
|     `13` | Sync A              | —               | ⬜      |            |
|     `14` | Listen A            | —               | ⬜      |            |
|     `17` | Pad 1 Effect B      | —               | ⬜      |            |
|     `18` | Pad 2 Effect B      | —               | ⬜      |            |
|     `19` | Pad 3 Effect B      | —               | ⬜      |            |
|     `1A` | Pad 4 Effect B      | —               | ⬜      |            |
|     `1B` | Pad 1 Sample B      | —               | ⬜      |            |
|     `1C` | Pad 2 Sample B      | —               | ⬜      |            |
|     `1D` | Pad 3 Sample B      | —               | ⬜      |            |
|     `1E` | Pad 4 Sample B      | —               | ⬜      |            |
|     `1F` | Pad 1 Loop B        | —               | ⬜      |            |
|     `20` | Pad 2 Loop B        | —               | ⬜      |            |
|     `21` | Pad 3 Loop B        | —               | ⬜      |            |
|     `22` | Pad 4 Loop B        | —               | ⬜      |            |
|     `27` | Cue B               | —               | ⬜      |            |
|     `28` | Play B              | —               | ⬜      |            |
|     `29` | Sync B              | —               | ⬜      |            |
|     `2A` | Listen B            | —               | ⬜      |            |
|     `2D` | Scratch             | —               | ⬜      |            |
|     `2E` | Magic               | —               | ⬜      |            |
|     `30` | Record              | —               | ⬜      |            |
|     `35` | Files               | —               | ⬜      |            |
|     `36` | Folders             | —               | ⬜      |            |
|     `39` | Mix Headphones      | —               | ⬜      |            |
|     `3A` | Cue/PFL Headphones  | —               | ⬜      |            |
|     `3B` | Headphones Volume - | —               | ⬜      |            |
|     `3C` | Headphones Volume + | —               | ⬜      |            |
|     `44` | Beat 1 A            | —               | ⬜      |            |
|     `45` | Beat 2 A            | —               | ⬜      |            |
|     `46` | Beat 3 A            | —               | ⬜      |            |
|     `47` | Beat 4 A            | —               | ⬜      |            |
|     `4C` | Beat 1 B            | —               | ⬜      |            |
|     `4D` | Beat 2 B            | —               | ⬜      |            |
|     `4E` | Beat 3 B            | —               | ⬜      |            |
|     `4F` | Beat 4 B            | —               | ⬜      |            |

---

# 15. Resultados experimentais

Esta seção será atualizada conforme os testes forem realizados.

## TEST-LED-001

**Objetivo:** verificar o comando global de LEDs.

**Mensagem enviada:**

```text
B0 7F 00
```

**Resultado esperado:**

Todos os LEDs desligados.

**Resultado observado:**

*Pendente.*

---

## TEST-LED-002

**Objetivo:** verificar o comando global de LEDs.

**Mensagem enviada:**

```text
B0 7F 7F
```

**Resultado esperado:**

Todos os LEDs ligados.

**Resultado observado:**

*Pendente.*

---

# 16. Diferenças entre documentação e hardware

Esta seção deverá registrar qualquer divergência encontrada.

Formato recomendado:

| Endereço | Especificação | Hardware | Diferença |
| -------: | ------------- | -------- | --------- |
|        — | —             | —        | —         |

Nenhuma divergência foi registrada até o momento.

---

# 17. Diferenças em relação ao Mixxx

O mapping do Mixxx será utilizado como fonte secundária para comparação.

Esta seção deverá responder:

* quais LEDs o Mixxx controla;
* quais endereços utiliza;
* se utiliza `7F`/`00`;
* se utiliza outros valores;
* quais LEDs não são utilizados;
* se existem diferenças entre o mapping e a documentação Hercules.

| LED            | Hercules | Mixxx | Resultado |
| -------------- | -------- | ----- | --------- |
| Pad 1 Effect A | `01`     | —     | Pendente  |
| Play A         | `12`     | —     | Pendente  |
| Sync A         | `13`     | —     | Pendente  |
| Beat 1 A       | `44`     | —     | Pendente  |

---

# 18. Questões em investigação

As seguintes questões ainda precisam ser respondidas experimentalmente:

* O canal MIDI padrão é realmente o canal 1?
* Todos os endereços documentados respondem individualmente?
* O comando `B0 7F 7F` realmente acende todos os LEDs da unidade?
* Existem LEDs que compartilham endereço?
* Existem valores intermediários entre `00` e `7F`?
* Os LEDs possuem diferentes níveis de intensidade?
* Alguns LEDs possuem comportamento dependente do modo do controlador?
* Os pads possuem comportamento diferente quando a sensibilidade está habilitada?
* O VU-meter responde apenas a `00`/`7F` ou aceita outros valores?
* O hardware aceita mensagens MIDI em outros canais?
* Existem comandos MIDI não documentados pela Hercules?

---

# 19. Fontes

## Fonte primária

**Hercules / DJUCED - DJ Control AIR Reference Manual**

Seção:

```text
D. DJ Control AIR MIDI messages
```

Subseção:

```text
3. MIDI Output = control on LEDs
```

Páginas 51 e 52.

A documentação oficial especifica os comandos de MIDI Output, incluindo os LEDs dos decks, mixer, navegador, VU-meter, controles centrais, headphones e painel frontal.

## Fonte secundária

Código-fonte do Mixxx:

```text
Hercules DJ Control AIR.midi.xml
```

e o respectivo script JavaScript do controlador.

Esses arquivos serão tratados como **implementações de referência**, não como especificação oficial.

---

# 20. Histórico de validação

| Data       | Teste                             | Resultado |
| ---------- | --------------------------------- | --------- |
| 2026-09-03 | Documentação oficial identificada | Concluído |
| 2026-09-03 | Mapa inicial dos LEDs             | Concluído |
| —          | Teste global OFF                  | Pendente  |
| —          | Teste global ON                   | Pendente  |
| —          | Teste individual dos LEDs         | Pendente  |
| —          | Comparação com Mixxx              | Pendente  |

---

## Referência principal

A especificação utilizada neste documento foi extraída da seção de MIDI Output do manual oficial **DJUCED™ and DJ Control AIR Reference Manual**, que documenta os LEDs e seus respectivos endereços MIDI.
