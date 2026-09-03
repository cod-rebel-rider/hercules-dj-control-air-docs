# Protocolo MIDI

Documentação do protocolo MIDI utilizado pelo **Hercules DJ Control AIR**.

> **Status:** Em documentação
> **Fonte principal:** documentação técnica oficial da Hercules
> **Última revisão:** 2026-09-03

---

## 1. Introdução

O Hercules DJ Control AIR utiliza o protocolo **MIDI (Musical Instrument Digital Interface)** para comunicação bidirecional com o computador.

A comunicação possui duas direções:

```text
Hercules DJ Control AIR
        │
        │ MIDI IN
        ▼
     Computador
        │
        │ MIDI OUT
        ▼
Hercules DJ Control AIR
```

### MIDI IN

Neste projeto, **MIDI IN** significa as mensagens enviadas pelo controlador para o computador.

Exemplos:

* pressionamento de botões;
* movimento de faders;
* movimento de knobs;
* movimento dos jog wheels;
* interação com os sensores.

### MIDI OUT

**MIDI OUT** significa as mensagens enviadas pelo computador para o controlador.

No DJ Control AIR, essas mensagens são utilizadas principalmente para:

* controlar LEDs;
* alterar o estado visual dos controles;
* atualizar o estado dos indicadores luminosos.

A documentação oficial da Hercules define explicitamente que os comandos MIDI OUT enviados pelo computador são recebidos pelo controlador e utilizados para controlar os LEDs.

---

# 2. Representação das mensagens

As mensagens MIDI deste documento são representadas em hexadecimal.

Uma mensagem MIDI de três bytes possui normalmente o formato:

```text
STATUS DATA1 DATA2
```

Onde:

| Campo    | Descrição                                  |
| -------- | ------------------------------------------ |
| `STATUS` | Define o tipo da mensagem e o canal MIDI   |
| `DATA1`  | Identifica o controle, nota ou controlador |
| `DATA2`  | Contém o valor associado à mensagem        |

Exemplo:

```text
90 12 7F
```

---

# 3. Canais MIDI

A documentação original utiliza a notação:

```text
9x
Bx
```

O `x` representa o canal MIDI.

Portanto:

```text
9x
```

representa uma mensagem **Note On** cujo canal pode variar.

Da mesma forma:

```text
Bx
```

representa uma mensagem **Control Change** cujo canal pode variar.

Para o canal MIDI 1:

```text
9x → 90
Bx → B0
```

Assim, quando a documentação oficial apresenta:

```text
9x 12 Value
```

a representação no canal MIDI 1 é:

```text
90 12 Value
```

---

# 4. Valores de botão

Os botões do DJ Control AIR utilizam valores digitais.

A convenção documentada pela Hercules é:

```text
7F = ligado / pressionado
00 = desligado / liberado
```

Portanto:

```text
90 12 7F
```

pode representar:

```text
Play Deck A = pressionado
```

Enquanto:

```text
90 12 00
```

representa:

```text
Play Deck A = liberado
```

---

# 5. Valores analógicos

Alguns controles utilizam valores MIDI contínuos.

O intervalo MIDI utilizado é:

```text
00 → 7F
```

ou, em decimal:

```text
0 → 127
```

A documentação classifica determinados controles como:

```text
Analog - Coarse (128 values)
```

Isso significa que o controle possui 128 posições representáveis no protocolo MIDI.

Exemplo:

```text
00 = posição mínima
7F = posição máxima
```

---

# 6. Mensagens MIDI de entrada

## 6.1 Deck A

### Pads

| Controle     | Mensagem      | Tipo  |
| ------------ | ------------- | ----- |
| Pad 1 Effect | `9x 01 Value` | Botão |
| Pad 2 Effect | `9x 02 Value` | Botão |
| Pad 3 Effect | `9x 03 Value` | Botão |
| Pad 4 Effect | `9x 04 Value` | Botão |
| Pad 1 Sample | `9x 05 Value` | Botão |
| Pad 2 Sample | `9x 06 Value` | Botão |
| Pad 3 Sample | `9x 07 Value` | Botão |
| Pad 4 Sample | `9x 08 Value` | Botão |
| Pad 1 Loop   | `9x 09 Value` | Botão |
| Pad 2 Loop   | `9x 0A Value` | Botão |
| Pad 3 Loop   | `9x 0B Value` | Botão |
| Pad 4 Loop   | `9x 0C Value` | Botão |

### Pitch

| Controle     | Mensagem      | Tipo  |
| ------------ | ------------- | ----- |
| Pitch Bend - | `9x 0D Value` | Botão |
| Pitch Bend + | `9x 0E Value` | Botão |

### Reprodução

| Controle    | Mensagem      | Tipo  |
| ----------- | ------------- | ----- |
| Cue Deck A  | `9x 11 Value` | Botão |
| Play Deck A | `9x 12 Value` | Botão |
| Sync Deck A | `9x 13 Value` | Botão |

---

# 7. Deck B

### Pads

| Controle     | Mensagem      | Tipo  |
| ------------ | ------------- | ----- |
| Pad 1 Effect | `9x 17 Value` | Botão |
| Pad 2 Effect | `9x 18 Value` | Botão |
| Pad 3 Effect | `9x 19 Value` | Botão |
| Pad 4 Effect | `9x 1A Value` | Botão |
| Pad 1 Sample | `9x 1B Value` | Botão |
| Pad 2 Sample | `9x 1C Value` | Botão |
| Pad 3 Sample | `9x 1D Value` | Botão |
| Pad 4 Sample | `9x 1E Value` | Botão |
| Pad 1 Loop   | `9x 1F Value` | Botão |
| Pad 2 Loop   | `9x 20 Value` | Botão |
| Pad 3 Loop   | `9x 21 Value` | Botão |
| Pad 4 Loop   | `9x 22 Value` | Botão |

### Pitch

| Controle     | Mensagem      | Tipo  |
| ------------ | ------------- | ----- |
| Pitch Bend - | `9x 23 Value` | Botão |
| Pitch Bend + | `9x 24 Value` | Botão |

### Reprodução

| Controle    | Mensagem      | Tipo  |
| ----------- | ------------- | ----- |
| Cue Deck B  | `9x 27 Value` | Botão |
| Play Deck B | `9x 28 Value` | Botão |
| Sync Deck B | `9x 29 Value` | Botão |

---

# 8. Mixer

## Faders

| Controle      | Mensagem      | Tipo      |
| ------------- | ------------- | --------- |
| Crossfader    | `Bx 3A Value` | Analógico |
| Volume Deck A | `Bx 36 Value` | Analógico |
| Volume Deck B | `Bx 3B Value` | Analógico |

Os faders utilizam valores:

```text
00 → 7F
```

representando a posição física do controle.

---

## Equalizador

### Deck A

| Controle  | Mensagem      | Tipo      |
| --------- | ------------- | --------- |
| EQ High A | `Bx 37 Value` | Analógico |
| EQ Mid A  | `Bx 38 Value` | Analógico |
| EQ Low A  | `Bx 39 Value` | Analógico |

### Deck B

| Controle  | Mensagem      | Tipo      |
| --------- | ------------- | --------- |
| EQ High B | `Bx 3C Value` | Analógico |
| EQ Mid B  | `Bx 3D Value` | Analógico |
| EQ Low B  | `Bx 3E Value` | Analógico |

---

# 9. Jog Wheels

Os jog wheels possuem mensagens MIDI próprias.

| Controle         | Mensagem      | Tipo     |
| ---------------- | ------------- | -------- |
| Jog Wheel Deck A | `Bx 30 Value` | Rotativo |
| Jog Wheel Deck B | `Bx 31 Value` | Rotativo |

Os jog wheels também possuem informações relacionadas ao modo de scratch e à interação com a superfície.

Esses comportamentos serão documentados separadamente na seção de testes experimentais.

---

# 10. Sensor AIR

O DJ Control AIR possui um sensor de proximidade conhecido como **Air Control**.

A mensagem documentada para o sensor é:

```text
Bx 3F Value
```

O comportamento e os valores efetivamente produzidos pelo sensor serão documentados experimentalmente.

---

# 11. Painel frontal

Os controles do painel frontal utilizam as seguintes mensagens:

| Controle                | Mensagem      | Tipo  |
| ----------------------- | ------------- | ----- |
| Mix in Headphones       | `9x 39 Value` | Botão |
| Cue (PFL) in Headphones | `9x 3A Value` | Botão |
| Headphones Volume -     | `9x 3B Value` | Botão |
| Headphones Volume +     | `9x 3C Value` | Botão |

Para os botões:

```text
7F = pressionado
00 = liberado
```

---

# 12. MIDI OUT e LEDs

O computador pode enviar mensagens MIDI para o DJ Control AIR para controlar seus LEDs.

A documentação oficial utiliza a mesma identificação dos controles.

## Deck A

### Pads Effect

| LED            | MIDI OUT      |  OFF |   ON |
| -------------- | ------------- | ---: | ---: |
| Pad 1 Effect A | `9x 01 Value` | `00` | `7F` |
| Pad 2 Effect A | `9x 02 Value` | `00` | `7F` |
| Pad 3 Effect A | `9x 03 Value` | `00` | `7F` |
| Pad 4 Effect A | `9x 04 Value` | `00` | `7F` |

### Pads Sample

| LED            | MIDI OUT      |  OFF |   ON |
| -------------- | ------------- | ---: | ---: |
| Pad 1 Sample A | `9x 05 Value` | `00` | `7F` |
| Pad 2 Sample A | `9x 06 Value` | `00` | `7F` |
| Pad 3 Sample A | `9x 07 Value` | `00` | `7F` |
| Pad 4 Sample A | `9x 08 Value` | `00` | `7F` |

### Pads Loop

| LED          | MIDI OUT      |  OFF |   ON |
| ------------ | ------------- | ---: | ---: |
| Pad 1 Loop A | `9x 09 Value` | `00` | `7F` |
| Pad 2 Loop A | `9x 0A Value` | `00` | `7F` |
| Pad 3 Loop A | `9x 0B Value` | `00` | `7F` |
| Pad 4 Loop A | `9x 0C Value` | `00` | `7F` |

### Reprodução

| LED    | MIDI OUT      |  OFF |   ON |
| ------ | ------------- | ---: | ---: |
| Cue A  | `9x 11 Value` | `00` | `7F` |
| Play A | `9x 12 Value` | `00` | `7F` |
| Sync A | `9x 13 Value` | `00` | `7F` |

---

# 13. LEDs do Deck B

### Pads Effect

| LED            | MIDI OUT      |  OFF |   ON |
| -------------- | ------------- | ---: | ---: |
| Pad 1 Effect B | `9x 17 Value` | `00` | `7F` |
| Pad 2 Effect B | `9x 18 Value` | `00` | `7F` |
| Pad 3 Effect B | `9x 19 Value` | `00` | `7F` |
| Pad 4 Effect B | `9x 1A Value` | `00` | `7F` |

### Pads Sample

| LED            | MIDI OUT      |  OFF |   ON |
| -------------- | ------------- | ---: | ---: |
| Pad 1 Sample B | `9x 1B Value` | `00` | `7F` |
| Pad 2 Sample B | `9x 1C Value` | `00` | `7F` |
| Pad 3 Sample B | `9x 1D Value` | `00` | `7F` |
| Pad 4 Sample B | `9x 1E Value` | `00` | `7F` |

### Pads Loop

| LED          | MIDI OUT      |  OFF |   ON |
| ------------ | ------------- | ---: | ---: |
| Pad 1 Loop B | `9x 1F Value` | `00` | `7F` |
| Pad 2 Loop B | `9x 20 Value` | `00` | `7F` |
| Pad 3 Loop B | `9x 21 Value` | `00` | `7F` |
| Pad 4 Loop B | `9x 22 Value` | `00` | `7F` |

### Reprodução

| LED    | MIDI OUT      |  OFF |   ON |
| ------ | ------------- | ---: | ---: |
| Cue B  | `9x 27 Value` | `00` | `7F` |
| Play B | `9x 28 Value` | `00` | `7F` |
| Sync B | `9x 29 Value` | `00` | `7F` |

---

# 14. LEDs do painel frontal

| LED                 | MIDI OUT      |  OFF |   ON |
| ------------------- | ------------- | ---: | ---: |
| Mix in Headphones   | `9x 39 Value` | `00` | `7F` |
| Cue/PFL Headphones  | `9x 3A Value` | `00` | `7F` |
| Headphones Volume - | `9x 3B Value` | `00` | `7F` |
| Headphones Volume + | `9x 3C Value` | `00` | `7F` |

---

# 15. Atualização de todos os LEDs

A Hercules documenta uma mensagem especial para atualizar todos os LEDs simultaneamente:

```text
Bx 7F Value
```

Valores:

```text
00 = todos os LEDs desligados
7F = todos os LEDs ligados
```

No canal MIDI 1:

### Todos ligados

```text
B0 7F 7F
```

### Todos desligados

```text
B0 7F 00
```

Este comando será utilizado posteriormente como um dos primeiros testes experimentais do projeto.

---

# 16. Notação oficial × representação prática

Para evitar ambiguidades, este projeto manterá a notação original da Hercules quando estiver reproduzindo a especificação:

```text
9x
Bx
```

Quando estivermos descrevendo um teste executado no canal MIDI 1, utilizaremos:

```text
90
B0
```

Exemplo:

### Especificação

```text
9x 12 Value
```

### Teste no canal 1

```text
90 12 7F
```

---

# 17. Fontes

## Documentação oficial

* Hercules DJ Control AIR / DJUCED Reference Manual.
* Seção de comandos MIDI.
* Seção de MIDI Output / LEDs.

## Implementações de referência

O projeto também será comparado posteriormente com o mapping existente no Mixxx:

`Hercules DJ Control AIR.midi.xml`

e:

`Hercules-DJ-Control-AIR-scripts.js`

Esses arquivos serão tratados como **implementações de referência**, e não como especificação oficial do hardware.

---

# 18. Classificação das informações

Cada informação adicionada ao projeto deverá ser classificada de acordo com sua origem.

| Classificação     | Significado                             |
| ----------------- | --------------------------------------- |
| **Oficial**       | Documentada pela Hercules               |
| **Implementação** | Encontrada em software compatível       |
| **Experimental**  | Confirmada através de teste físico      |
| **Inferência**    | Deduzida a partir de outras informações |
| **Desconhecido**  | Ainda não confirmado                    |

Essa classificação é importante para evitar que uma hipótese ou comportamento observado em uma versão específica do software seja apresentado como especificação oficial do controlador.

---

# 19. Próximos testes

Os próximos testes experimentais deverão confirmar:

* canal MIDI utilizado pelo hardware;
* mensagens efetivamente enviadas pelos botões;
* comportamento dos pads;
* comportamento dos jog wheels;
* resposta do sensor AIR;
* correspondência física entre endereço MIDI e LED;
* funcionamento do comando de atualização de todos os LEDs;
* comportamento de valores diferentes de `00` e `7F`;
* comportamento dos LEDs durante o uso do DJUCED;
* diferenças entre a especificação Hercules e o mapping do Mixxx.

---

## Referência

A documentação oficial da Hercules identifica explicitamente as mensagens MIDI do DJ Control AIR e documenta o MIDI Output como mecanismo de controle dos LEDs.
