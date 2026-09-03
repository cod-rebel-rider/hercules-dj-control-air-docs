import mido


EXPECTED_IN = "DJ Control Air 0"
EXPECTED_OUT = "DJ Control Air 1"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    print("Hercules DJ Control AIR - MIDI Probe")
    print("------------------------------------")

    # ==========================================================
    # MIDI INPUT
    # ==========================================================

    print_section("PORTAS MIDI IN")

    input_ports = mido.get_input_names()

    if not input_ports:
        print("Nenhuma porta MIDI IN encontrada.")
    else:
        for index, name in enumerate(input_ports, start=1):
            print(f"{index}. {name}")

    # ==========================================================
    # MIDI OUTPUT
    # ==========================================================

    print_section("PORTAS MIDI OUT")

    output_ports = mido.get_output_names()

    if not output_ports:
        print("Nenhuma porta MIDI OUT encontrada.")
    else:
        for index, name in enumerate(output_ports, start=1):
            print(f"{index}. {name}")

    # ==========================================================
    # DETECÇÃO DA HERCULES
    # ==========================================================

    print_section("DETECÇÃO DA DJ CONTROL AIR")

    detected_in = [
        name for name in input_ports
        if "DJ Control Air" in name
    ]

    detected_out = [
        name for name in output_ports
        if "DJ Control Air" in name
    ]

    if detected_in:
        print("MIDI IN detectado:")
        for name in detected_in:
            print(f"  OK  {name}")
    else:
        print("MIDI IN da DJ Control AIR não encontrado.")

    if detected_out:
        print("MIDI OUT detectado:")
        for name in detected_out:
            print(f"  OK  {name}")
    else:
        print("MIDI OUT da DJ Control AIR não encontrado.")

    # ==========================================================
    # PORTAS ESPERADAS
    # ==========================================================

    print_section("PORTAS ESPERADAS")

    if EXPECTED_IN in input_ports:
        print(f"[OK] MIDI IN  : {EXPECTED_IN}")
    else:
        print(f"[ERRO] MIDI IN não encontrado: {EXPECTED_IN}")

    if EXPECTED_OUT in output_ports:
        print(f"[OK] MIDI OUT : {EXPECTED_OUT}")
    else:
        print(f"[ERRO] MIDI OUT não encontrado: {EXPECTED_OUT}")

    # ==========================================================
    # TESTE DE ABERTURA MIDI IN
    # ==========================================================

    print_section("TESTE MIDI IN")

    if EXPECTED_IN in input_ports:
        try:
            with mido.open_input(EXPECTED_IN):
                print(f"[OK] Foi possível abrir: {EXPECTED_IN}")
        except Exception as error:
            print(f"[ERRO] Não foi possível abrir {EXPECTED_IN}")
            print(f"       {error}")
    else:
        print("[IGNORADO] Porta MIDI IN não encontrada.")

    # ==========================================================
    # TESTE DE ABERTURA MIDI OUT
    # ==========================================================

    print_section("TESTE MIDI OUT")

    if EXPECTED_OUT in output_ports:
        try:
            with mido.open_output(EXPECTED_OUT):
                print(f"[OK] Foi possível abrir: {EXPECTED_OUT}")
        except Exception as error:
            print(f"[ERRO] Não foi possível abrir {EXPECTED_OUT}")
            print(f"       {error}")
    else:
        print("[IGNORADO] Porta MIDI OUT não encontrada.")

    # ==========================================================
    # CONFIGURAÇÃO CONHECIDA
    # ==========================================================

    print_section("CONFIGURAÇÃO ATUAL CONHECIDA")

    print("Controlador : Hercules DJ Control AIR")
    print("MIDI IN     : DJ Control Air 0")
    print("MIDI OUT    : DJ Control Air 1")
    print("Canal MIDI  : 2")
    print("Mido channel: 1 (0-based)")

    print()
    print("LED confirmado:")
    print("  Play/Pause Deck A")
    print("  ON  = 91 12 7F")
    print("  OFF = 91 12 00")

    print()
    print("Probe concluído.")


if __name__ == "__main__":
    main()