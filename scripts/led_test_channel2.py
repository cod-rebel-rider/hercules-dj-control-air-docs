import mido
import time

PORT_NAME = "DJ Control Air 1"

print(f"Abrindo MIDI OUT: {PORT_NAME}")

with mido.open_output(PORT_NAME) as port:
    print("Enviando Play A LED ON:")
    print("91 12 7F")

    port.send(
        mido.Message(
            "note_on",
            channel=1,
            note=0x12,
            velocity=0x7F
        )
    )

    time.sleep(2)

    print("Enviando Play A LED OFF:")
    print("91 12 00")

    port.send(
        mido.Message(
            "note_on",
            channel=1,
            note=0x12,
            velocity=0x00
        )
    )