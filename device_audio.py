import sounddevice as sd
print(sd.query_devices())


def list_input_devices():
    devices = sd.query_devices()
    input_devices = [device for device in devices if device['max_input_channels'] > 0]
    return input_devices

def get_default_input_device():
    default_device = sd.default.device[0]  # Le premier élément est l'appareil d'entrée par défaut
    return default_device

# Lister tous les périphériques d'entrée
input_devices = list_input_devices()
print("Périphériques d'entrée détectés :")
for idx, device in enumerate(input_devices):
    print(f"{idx}: {device['name']} (Channels: {device['max_input_channels']})")

# Obtenir et imprimer l'appareil d'entrée par défaut
default_input_device = get_default_input_device()
print(f"\nAppareil d'entrée par défaut ID: {default_input_device}")
print(f"Nom du périphérique d'entrée par défaut : {sd.query_devices(default_input_device)['name']}")
