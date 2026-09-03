import sys


def usage():
    print("Uso:")
    print("  py midi_decode.py <byte1> <byte2> <byte3>")
    print()
    print("Exemplos:")
    print("  py midi_decode.py 91 12 7F")
    print("  py midi_decode.py B1 30 40")
    print()


def parse_byte(value):
    try:
        byte = int(value, 16)
    except ValueError:
        raise ValueError(
            f"'{value}' não é um byte hexadecimal válido."
        )

    if not 0x00 <= byte <= 0xFF:
        raise ValueError(
            f"'{value}' está fora do intervalo 00-FF."
        )

    return byte


def decode(status, data1, data2):

    message_type = status & 0xF0
    channel = (status & 0x0F) + 1

    print()
    print("=" * 50)
    print("MIDI DECODE")
    print("=" * 50)

    print(f"Bytes:    {status:02X} {data1:02X} {data2:02X}")
    print(f"Canal:    {channel}")

    if message_type == 0x80:
        print("Tipo:     Note Off")
        print(f"Nota:     {data1:02X}")
        print(f"Velocity: {data2:02X}")

    elif message_type == 0x90:
        print("Tipo:     Note On")
        print(f"Nota:     {data1:02X}")
        print(f"Velocity: {data2:02X}")

        if data2 == 0:
            print("Estado:   OFF")
        else:
            print("Estado:   ON")

    elif message_type == 0xA0:
        print("Tipo:     Poly Pressure")
        print(f"Nota:     {data1:02X}")
        print(f"Valor:    {data2:02X}")

    elif message_type == 0xB0:
        print("Tipo:     Control Change")
        print(f"Controle: {data1:02X}")
        print(f"Valor:    {data2:02X}")

    elif message_type == 0xC0:
        print("Tipo:     Program Change")
        print(f"Programa: {data1:02X}")

    elif message_type == 0xD0:
        print("Tipo:     Channel Pressure")
        print(f"Valor:    {data1:02X}")

    elif message_type == 0xE0:
        print("Tipo:     Pitch Bend")

        value = data1 | (data2 << 7)
        value -= 8192

        print(f"Valor bruto: {data1:02X} {data2:02X}")
        print(f"Valor:       {value}")

    else:
        print("Tipo:     Mensagem desconhecida")


def main():

    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    try:
        status = parse_byte(sys.argv[1])
        data1 = parse_byte(sys.argv[2])
        data2 = parse_byte(sys.argv[3])

        if status < 0x80:
            raise ValueError(
                "O primeiro byte precisa ser um byte de status (80-FF)."
            )

        decode(status, data1, data2)

    except ValueError as error:
        print(f"Erro: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()