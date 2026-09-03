import mido

PORT_NAME = "DJ Control Air 0"

print("Portas MIDI IN:")
for name in mido.get_input_names():
    print(f"  - {name}")

print(f"\nAbrindo MIDI IN: {PORT_NAME}")

with mido.open_input(PORT_NAME) as port:
    print("Monitor ativo.")
    print("Pressione PLAY, CUE, SYNC e mexa nos controles.")
    print("Ctrl+C para sair.\n")

    for message in port:
        print(message)