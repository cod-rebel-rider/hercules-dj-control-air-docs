# Protocolo MIDI

## Introdução

O Hercules DJ Control AIR utiliza comunicação MIDI para transmitir informações dos controles físicos ao computador e receber comandos destinados ao controlador.

A comunicação será documentada neste projeto utilizando valores em hexadecimal.

## Formato

As mensagens MIDI serão representadas neste formato:

```text
STATUS DATA1 DATA2
```

Exemplo:

```text
90 01 7F
```

Onde:

| Campo | Descrição |
| --- | --- |
| STATUS | Tipo da mensagem e canal MIDI |
| DATA1 | Identificador do controle |
| DATA2 | Valor da mensagem |

## Tipos observados

### Note On

Formato:

```text
90 NN VV
```

Onde:

- `90` = Note On no canal MIDI 1;
- `NN` = número da nota/controle;
- `VV` = valor.

### Control Change

Formato:

```text
B0 CC VV
```

Onde:

- `B0` = Control Change no canal MIDI 1;
- `CC` = número do controlador;
- `VV` = valor.

## Convenção deste documento

Valores MIDI serão apresentados em hexadecimal, salvo indicação contrária.
