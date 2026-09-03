import json
import os
import time
from datetime import datetime

import mido


PORT_NAME = "DJ Control Air 0"
RESULT_FILE = "control-test-results.json"

CAPTURE_TIME = 3.0


TESTS = [
    {
        "id": "PLAY_A",
        "name": "Play/Pause Deck A",
    },
    {
        "id": "CUE_A",
        "name": "Cue Deck A",
    },
    {
        "id": "SYNC_A",
        "name": "Sync Deck A",
    },
    {
        "id": "PLAY_B",
        "name": "Play/Pause Deck B",
    },
    {
        "id": "CUE_B",
        "name": "Cue Deck B",
    },
    {
        "id": "SYNC_B",
        "name": "Sync Deck B",
    },
    {
        "id": "PAD_A_01",
        "name": "Pad 1 Deck A",
    },
    {
        "id": "PAD_A_02",
        "name": "Pad 2 Deck A",
    },
    {
        "id": "PAD_A_03",
        "name": "Pad 3 Deck A",
    },
    {
        "id": "PAD_A_04",
        "name": "Pad 4 Deck A",
    },
    {
        "id": "PAD_B_01",
        "name": "Pad 1 Deck B",
    },
    {
        "id": "PAD_B_02",
        "name": "Pad 2 Deck B",
    },
    {
        "id": "PAD_B_03",
        "name": "Pad 3 Deck B",
    },
    {
        "id": "PAD_B_04",
        "name": "Pad 4 Deck B",
    },
    {
        "id": "JOG_A",
        "name": "Jog Wheel Deck A",
    },
    {
        "id": "JOG_B",
        "name": "Jog Wheel Deck B",
    },
    {
        "id": "SCRATCH_A",
        "name": "Scratch Jog Deck A",
    },
    {
        "id": "SCRATCH_B",
        "name": "Scratch Jog Deck B",
    },
]


def message_to_hex(message):
    return " ".join(
        f"{byte:02X}"
        for byte in message.bytes()
    )


def describe_message(message):
    if message.type == "note_on":
        state = "ON" if message.velocity else "OFF"

        return (
            f"Note {message.note:02X} "
            f"velocity={message.velocity:02X} "
            f"{state}"
        )

    if message.type == "note_off":
        return (
            f"Note Off "
            f"{message.note:02X} "
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


def load_results():
    if not os.path.exists(RESULT_FILE):
        return {}

    try:
        with open(
            RESULT_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return {}


def save_results(results):
    with open(
        RESULT_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )


def capture(port, duration):
    messages = []

    end_time = time.monotonic() + duration

    while time.monotonic() < end_time:

        for message in port.iter_pending():

            messages.append({
                "hex": message_to_hex(message),
                "type": message.type,
                "description": describe_message(message),
                "bytes": message.bytes(),
            })

        time.sleep(0.01)

    return messages


def print_messages(messages):

    if not messages:
        print()
        print("Nenhuma mensagem capturada.")
        return

    print()
    print("Mensagens capturadas:")
    print("---------------------")

    for index, message in enumerate(
        messages,
        start=1
    ):
        print(
            f"{index:02d}. "
            f"{message['hex']:<12} "
            f"{message['description']}"
        )


def main():

    print("Hercules DJ Control AIR - Control Test")
    print("======================================")
    print()
    print(f"MIDI IN: {PORT_NAME}")
    print(f"Tempo de captura: {CAPTURE_TIME:.1f}s")
    print()

    results = load_results()

    with mido.open_input(PORT_NAME) as port:

        for test in TESTS:

            test_id = test["id"]
            test_name = test["name"]

            if test_id in results:

                print(
                    f"[JÁ TESTADO] "
                    f"{test_id} - {test_name}"
                )

                continue

            print()
            print("=" * 60)
            print(f"TESTE: {test_id}")
            print(f"CONTROLE: {test_name}")
            print("=" * 60)

            print()
            print("Prepare o controle.")
            input("Pressione ENTER para começar...")

            # Limpa mensagens antigas antes do teste
            for _ in port.iter_pending():
                pass

            print()
            print(">>> EXECUTE A AÇÃO AGORA <<<")
            print(
                f">>> Capturando por "
                f"{CAPTURE_TIME:.1f} segundos..."
            )

            messages = capture(
                port,
                CAPTURE_TIME
            )

            print()
            print("Captura finalizada.")

            print_messages(messages)

            result = {
                "id": test_id,
                "name": test_name,
                "timestamp": datetime.now().isoformat(),
                "messages": messages,
            }

            results[test_id] = result

            save_results(results)

            print()
            print(
                f"Resultado salvo em "
                f"{RESULT_FILE}"
            )

    print()
    print("=" * 60)
    print("TESTES CONCLUÍDOS")
    print("=" * 60)


if __name__ == "__main__":
    main()