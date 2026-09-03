import json
import mido
import os
import time


PORT_NAME = "DJ Control Air 1"
MIDI_CHANNEL = 1  # Mido é 0-based: 1 = MIDI Channel 2

RESULT_FILE = "led-scan-results.json"

# Endereços conhecidos/documentados para LEDs
LED_ADDRESSES = [
    0x01, 0x02, 0x03, 0x04,
    0x05, 0x06, 0x07, 0x08,
    0x09, 0x0A, 0x0B, 0x0C,
    0x11, 0x12, 0x13,
    0x17, 0x18, 0x19, 0x1A,
    0x1B, 0x1C, 0x1D, 0x1E,
    0x1F, 0x20, 0x21, 0x22,
    0x27, 0x28, 0x29,
    0x2D, 0x2E, 0x30,
    0x35, 0x36,
    0x39, 0x3A, 0x3B, 0x3C,
    0x44, 0x45, 0x46, 0x47,
    0x4C, 0x4D, 0x4E, 0x4F,
]


def send_led(port, note, state):
    velocity = 0x7F if state else 0x00

    port.send(
        mido.Message(
            "note_on",
            channel=MIDI_CHANNEL,
            note=note,
            velocity=velocity
        )
    )


def load_results():
    if not os.path.exists(RESULT_FILE):
        return {}

    try:
        with open(RESULT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}


def save_results(results):
    with open(RESULT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )


def ask_result():
    print()
    print("Qual foi o resultado?")
    print("  y = LED acendeu")
    print("  n = nenhum LED")
    print("  m = múltiplos LEDs")
    print("  s = pular")
    print()

    while True:
        answer = input("> ").strip().lower()

        if answer in ("y", "n", "m", "s"):
            return answer

        print("Resposta inválida. Use y, n, m ou s.")


def main():
    print("Hercules DJ Control AIR - LED Scanner")
    print("=====================================")
    print()
    print(f"MIDI OUT : {PORT_NAME}")
    print(f"Canal    : {MIDI_CHANNEL + 1}")
    print(f"Total de endereços: {len(LED_ADDRESSES)}")
    print()

    results = load_results()

    with mido.open_output(PORT_NAME) as port:

        for index, note in enumerate(LED_ADDRESSES, start=1):

            key = f"{note:02X}"

            if key in results:
                print(
                    f"[{index}/{len(LED_ADDRESSES)}] "
                    f"{key} já registrado como "
                    f"{results[key]['result']}. Pulando."
                )
                continue

            print()
            print("=" * 50)
            print(
                f"[{index}/{len(LED_ADDRESSES)}] "
                f"Testando endereço {key}"
            )
            print("=" * 50)

            print()
            print(f"Comando ON: 91 {key} 7F")

            send_led(port, note, True)

            time.sleep(1)

            result = ask_result()

            # Desliga imediatamente depois da observação
            print(f"Comando OFF: 91 {key} 00")

            send_led(port, note, False)

            time.sleep(0.3)

            results[key] = {
                "result": {
                    "y": "led",
                    "n": "none",
                    "m": "multiple",
                    "s": "skipped"
                }[result],
                "command_on": f"91 {key} 7F",
                "command_off": f"91 {key} 00"
            }

            save_results(results)

            print()
            print(f"Resultado salvo: {key} = {results[key]['result']}")

    print()
    print("=" * 50)
    print("SCAN CONCLUÍDO")
    print("=" * 50)
    print()
    print(f"Resultados salvos em: {RESULT_FILE}")


if __name__ == "__main__":
    main()