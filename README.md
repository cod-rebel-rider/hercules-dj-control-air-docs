# Hercules DJ Control AIR - Documentação Técnica

Documentação técnica independente do controlador MIDI Hercules DJ Control AIR.

Este projeto reúne informações sobre:

- controles físicos;
- mensagens MIDI de entrada (MIDI IN);
- mensagens MIDI de saída (MIDI OUT);
- LEDs;
- jog wheels;
- sensores;
- comportamento dos botões;
- comunicação com softwares de DJ;
- testes experimentais;
- compatibilidade com o Mixxx.

## Objetivo

Documentar o protocolo MIDI e o comportamento do Hercules DJ Control AIR de forma clara e reproduzível.

A documentação diferencia:

- **Oficial**: informação encontrada na documentação da Hercules;
- **Implementação**: informação encontrada em softwares como o Mixxx;
- **Experimental**: comportamento observado diretamente no controlador;
- **Inferência**: informação deduzida a partir das outras fontes.

## Fontes

- Documentação técnica da Hercules;
- Documentação do DJUCED;
- Código-fonte do Mixxx;
- Testes realizados diretamente no Hercules DJ Control AIR.

## Estrutura

- [`docs/hardware/controles.md`](docs/hardware/controles.md) - controles e características físicas;
- [`docs/midi/protocolo.md`](docs/midi/protocolo.md) - protocolo MIDI;
- [`docs/leds/mapa-leds.md`](docs/leds/mapa-leds.md) - controle dos LEDs;
- [`testes/`](testes/) - testes experimentais;
- [`scripts/`](scripts/) - ferramentas auxiliares.

## Status

Em desenvolvimento.