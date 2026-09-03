import mido
from datetime import datetime


PORT_NAME = "DJ Control Air 0"
LOG_FILE = "midi-capture.log"


def message_to_hex(message):
    """
    Converte uma mensagem Mido para bytes MIDI em hexadecimal.
    """
    return " ".join(f"{byte:02X}" for byte in message.bytes())


def describe_message(message):
    """
    Retorna uma descrição amigável da mensagem.
    """

    if message.type == "note_on":
        state = "ON" if message.velocity > 0 else "OFF"

        return (
            f"Note {message.note:02X} "
            f"velocity={message.velocity:02X} "
            f"[{state}]"
        )

    if message.type == "note_off":
        return (
            f"Note {message.note:02X} "
            f"velocity={message.velocity:02X}"
        )

    if message.type == "control_change":
        return (
            f"CC {message.control:02X} "
            f"value={message.value:02X}"
        )

    if message.type == "polytouch":
        return (
            f"Poly Pressure "
            f"note={message.note:02X} "
            f"value={message.value:02X}"
        )

    if message.type == "aftertouch":
        return (
            f"Channel Pressure "
            f"value={message.value:02X}"
        )

    if message.type == "pitchwheel":
        return (
            f"Pitch Wheel "
            f"value={message.pitch}"
        )

    return message.type


def format_message(message):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    raw = message_to_hex(message)
    description = describe_message(message)

    return (
        f"{timestamp} | "
        f"{raw:<12} | "
        f"{description:<35} | "
        f"{message}"
    )


def main():

    print("Hercules DJ Control AIR - MIDI Capture")
    print("======================================")
    print()
    print(f"MIDI IN : {PORT_NAME}")
    print(f"Log     : {LOG_FILE}")
    print()
    print("Faça os movimentos que deseja analisar.")
    print("Ctrl+C para encerrar.")
    print()

    with mido.open_input(PORT_NAME) as port:

        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as log:

            log.write("\n")
            log.write(
                f"=== CAPTURE {datetime.now().isoformat()} ===\n"
            )

            try:

                for message in port:

                    line = format_message(message)

                    print(line)

                    log.write(line + "\n")
                    log.flush()

            except KeyboardInterrupt:

                print()
                print("Captura encerrada.")

                log.write(
                    f"=== END {datetime.now().isoformat()} ===\n"
                )


if __name__ == "__main__":
    main()
    