import mido
import time

PORT_NAME = "DJ Control Air 1"
MIDI_CHANNEL = 1  # Mido usa 0-based: 1 = MIDI Channel 2

print(f"Abrindo MIDI OUT: {PORT_NAME}")

with mido.open_output(PORT_NAME) as port:
    print()
    print("Teste global de LEDs")
    print("--------------------")
    print("Enviando todos os LEDs: OFF")
    print("B1 7F 00")

    port.send(
        mido.Message(
            "control_change",
            channel=MIDI_CHANNEL,
            control=0x7F,
            value=0x00
        )
    )

    time.sleep(1)

    print("Enviando todos os LEDs: ON")
    print("B1 7F 7F")

    port.send(
        mido.Message(
            "control_change",
            channel=MIDI_CHANNEL,
            control=0x7F,
            value=0x7F
        )
    )

    print()
    print("Teste concluído.")