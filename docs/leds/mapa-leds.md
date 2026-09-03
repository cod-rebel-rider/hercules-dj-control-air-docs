# Mapa de LEDs

## Introdução

O Hercules DJ Control AIR possui LEDs controlados pelo computador através de mensagens MIDI de saída.

A documentação oficial da Hercules será utilizada como referência primária.

## Convenção

Para os testes, utilizaremos:

### Ligar LED

```text
90 NN 7F
```

### Desligar LED

```text
90 NN 00
```

Onde `NN` identifica o LED.

## Deck A

| LED | MIDI OUT | Ligar | Desligar | Status |
| --- | --- | --- | --- | --- |
| Pad 1 Effect | `90 01` | `7F` | `00` | Documentado |
| Pad 2 Effect | `90 02` | `7F` | `00` | Documentado |
| Pad 3 Effect | `90 03` | `7F` | `00` | Documentado |
| Pad 4 Effect | `90 04` | `7F` | `00` | Documentado |
| Pad 1 Sample | `90 05` | `7F` | `00` | Documentado |
| Pad 2 Sample | `90 06` | `7F` | `00` | Documentado |
| Pad 3 Sample | `90 07` | `7F` | `00` | Documentado |
| Pad 4 Sample | `90 08` | `7F` | `00` | Documentado |
| Pad 1 Loop | `90 09` | `7F` | `00` | Documentado |
| Pad 2 Loop | `90 0A` | `7F` | `00` | Documentado |
| Pad 3 Loop | `90 0B` | `7F` | `00` | Documentado |
| Pad 4 Loop | `90 0C` | `7F` | `00` | Documentado |
| Cue | `90 11` | `7F` | `00` | Documentado |
| Play/Pause | `90 12` | `7F` | `00` | Documentado |
| Sync | `90 13` | `7F` | `00` | Documentado |

## Teste geral

Comando documentado para atualização dos LEDs:

```text
B0 7F 7F
```

Comando para desligar:

```text
B0 7F 00
```

## Testes experimentais

Os comandos acima serão testados diretamente no controlador para confirmar:

- se o LED responde;
- qual LED físico corresponde ao endereço;
- se o comportamento é momentâneo ou persistente;
- se existem estados intermediários;
- se há diferenças entre as unidades de hardware.