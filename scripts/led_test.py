import mido
import sys
import time

PORT_NAME = "DJ Control Air 1"
MIDI_CHANNEL = 1  # Mido usa 0-based: 1 = MIDI Channel 2


def print_usage():
    print("Uso:")
    print("  py led_test.py <nota>")
    print("  py led_test.py <nota> off")
    print()
    print("Exemplos:")
    print("  py led_test.py 12")
    print("  py led_test.py 12 off")
    print()
    print("O endereço deve ser informado em hexadecimal.")


if len(sys.argv) < 2:
    print_usage()
    sys.exit(1)


try:
    note = int(sys.argv[1], 16)
except ValueError:
    print(f"Erro: '{sys.argv[1]}' não é um endereço hexadecimal válido.")
    sys.exit(1)


if not 0x00 <= note <= 0x7F:
    print("Erro: o endereço deve estar entre 00 e 7F.")
    sys.exit(1)


if len(sys.argv) >= 3 and sys.argv[2].lower() == "off":
    velocity = 0x00
    state = "OFF"
else:
    velocity = 0x7F
    state = "ON"


status = 0x90 | MIDI_CHANNEL

print(f"Porta MIDI OUT : {PORT_NAME}")
print(f"Canal MIDI     : {MIDI_CHANNEL + 1}")
print(f"Nota           : {note:02X}")
print(f"Velocidade     : {velocity:02X}")
print(f"Estado         : {state}")
print(f"Comando        : {status:02X} {note:02X} {velocity:02X}")
print()

with mido.open_output(PORT_NAME) as port:
    port.send(
        mido.Message(
            "note_on",
            channel=MIDI_CHANNEL,
            note=note,
            velocity=velocity
        )
    )

    print("Comando enviado.")

    time.sleep(1)

