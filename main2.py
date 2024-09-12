# main.py

from recorder import SoundReceiverModule
from stt import SpeechToText
from diarization import SpeakerDiarization
import time
import os
import threading

# Fonction pour démarrer l'enregistrement audio
def start_recording():
    recorder = SoundReceiverModule(output_wav_file=output_audio_file,
                                   output_speech_detected_file=output_text_file,
                                   channel=1,  # Utilisez la configuration correcte
                                   seconds_to_keep=15,
                                   sample_rate=44100,
                                   loudness_threshold=0.01)
    try:
        recorder.start()
    except KeyboardInterrupt:
        print("Arrêt de l'enregistrement...")
        recorder.stop()



# # Fonction pour démarrer la reconnaissance vocale (STT)
def start_stt():
    stt = SpeechToText("medium", output_audio_file, output_text_file)
    try:
        stt.start()  # Cette méthode devrait traiter l'audio en continu
    except KeyboardInterrupt:
        print("Arrêt du traitement STT...")

# # Définition des chemins pour les fichiers audio et texte
AUDIOPATH = os.getenv("AUDIOPATH", "./")
TEXTPATH = os.getenv("TEXTPATH", "./")
output_audio_file = os.path.join(AUDIOPATH, "enregistrement_continue.wav")
output_text_file = os.path.join(TEXTPATH, "sortie.txt")

# # Création des threads pour l'enregistrement audio et le STT en simultané
recording_thread = threading.Thread(target=start_recording)
stt_thread = threading.Thread(target=start_stt)

# # Démarrage des deux threads
recording_thread.start()
stt_thread.start()

# # Attente de la fin des threads
recording_thread.join()
stt_thread.join()

print("Enregistrement et STT terminés.")
