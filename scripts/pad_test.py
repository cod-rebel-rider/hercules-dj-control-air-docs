import json
import os
import time
from datetime import datetime

import mido


PORT_NAME = "DJ Control Air 0"
RESULT_FILE = "pad-test-results.json"
CAPTURE_TIME = 4.0


PADS = [
    {"id": "PAD_A_01", "name": "Pad 1 Deck A", "note": 0x09},
    {"id": "PAD_A_02", "name": "Pad 2 Deck A", "note": 0x0A},
    {"id": "PAD_A_03", "name": "Pad 3 Deck A", "note": 0x0B},
    {"id": "PAD_A_04", "name": "Pad 4 Deck A", "note": 0x0C},

    {"id": "PAD_B_01", "name": "Pad 1 Deck B", "note": 0x1F},
    {"id": "PAD_B_02", "name": "Pad 2 Deck B", "note": 0x20},
    {"id": "PAD_B_03", "name": "Pad 3 Deck B", "note": 0x21},
    {"id": "PAD_B_04", "name": "Pad 4 Deck B", "note": 0x22},
]


def message_to_hex(message):
    return " ".join(f"{byte:02X}" for byte in message.bytes())


def capture(port, duration, target_note):
    messages = []

    end_time = time.monotonic() + duration

    while time.monotonic() < end_time:

        for message in port.iter_pending():

            # Ignora mensagens que não pertencem ao pad em teste
            if message.type in ("note_on", "note_off", "polytouch"):
                if message.note != target_note:
                    continue

            messages.append({
                "timestamp": datetime.now().isoformat(timespec="milliseconds"),
                "hex": message_to_hex(message),
                "type": message.type,
                "bytes": message.bytes(),
                "note": getattr(message, "note", None),
                "velocity": getattr(message, "velocity", None),
                "value": getattr(message, "value", None),
            })

        time.sleep(0.005)

    return messages


def analyze(messages, target_note):

    note_on = []
    note_off = []
    pressure = []

    for message in messages:

        if message["type"] == "note_on":
            if message["note"] == target_note:

                if message["velocity"] > 0:
                    note_on.append(message["velocity"])

                else:
                    note_off.append(message["velocity"])

        elif message["type"] == "note_off":
            if message["note"] == target_note:
                note_off.append(message["velocity"])

        elif message["type"] == "polytouch":
            if message["note"] == target_note:
                pressure.append(message["value"])

    return {
        "note_on_count": len(note_on),
        "note_on_values": note_on,
        "note_on_min": min(note_on) if note_on else None,
        "note_on_max": max(note_on) if note_on else None,

        "note_off_count": len(note_off),

        "pressure_count": len(pressure),
        "pressure_values": pressure,
        "pressure_min": min(pressure) if pressure else None,
        "pressure_max": max(pressure) if pressure else None,
    }


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


def print_messages(messages):

    if not messages:
        print()
        print("Nenhuma mensagem capturada.")
        return

    print()
    print("Mensagens:")
    print("----------")

    for index, message in enumerate(messages, start=1):

        print(
            f"{index:02d}. "
            f"{message['hex']:<12} "
            f"{message['type']}"
        )


def print_analysis(analysis):

    print()
    print("ANÁLISE")
    print("-------")

    print(
        f"Note On : {analysis['note_on_count']} "
        f"(min={analysis['note_on_min']}, "
        f"max={analysis['note_on_max']})"
    )

    print(
        f"Note Off: {analysis['note_off_count']}"
    )

    print(
        f"Pressure: {analysis['pressure_count']} "
        f"(min={analysis['pressure_min']}, "
        f"max={analysis['pressure_max']})"
    )


def main():

    print("Hercules DJ Control AIR - Pad Test")
    print("===================================")
    print()
    print(f"MIDI IN : {PORT_NAME}")
    print(f"Arquivo : {RESULT_FILE}")
    print()

    results = load_results()

    with mido.open_input(PORT_NAME) as port:

        for pad in PADS:

            test_id = pad["id"]
            test_name = pad["name"]
            target_note = pad["note"]

            if test_id in results:

                print(
                    f"[JÁ TESTADO] "
                    f"{test_id} - {test_name}"
                )

                continue

            print()
            print("=" * 65)
            print(f"TESTE: {test_id}")
            print(f"CONTROLE: {test_name}")
            print(f"NOTA ESPERADA: {target_note:02X}")
            print("=" * 65)

            print()
            print("O teste deve ser feito assim:")
            print("1. Pressione o pad normalmente.")
            print("2. Mantenha o pad pressionado.")
            print("3. Varie a força da pressão.")
            print("4. Solte o pad.")
            print()
            print(
                "Isso é importante para descobrir "
                "velocidade e Aftertouch/Poly Pressure."
            )

            input(
                "\nPressione ENTER para começar..."
            )

            # Limpa mensagens antigas
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
                CAPTURE_TIME,
                target_note
            )

            analysis = analyze(
                messages,
                target_note
            )

            print()
            print("Captura finalizada.")

            print_messages(messages)
            print_analysis(analysis)

            result = {
                "id": test_id,
                "name": test_name,
                "expected_note": f"{target_note:02X}",
                "timestamp": datetime.now().isoformat(),
                "messages": messages,
                "analysis": analysis,
            }

            results[test_id] = result

            save_results(results)

            print()
            print(
                f"Resultado salvo em {RESULT_FILE}"
            )

    print()
    print("=" * 65)
    print("TESTES DE PADS CONCLUÍDOS")
    print("=" * 65)


if __name__ == "__main__":
    main()