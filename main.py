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

# Ajout de la fonction pour démarrer la diarisation
def start_diarization():
    diarization = SpeakerDiarization(output_audio_file)
    segments = diarization.diarize()  # Obtenir les segments des locuteurs
    for start, end, speaker in segments:
        print(f"Locuteur {speaker} de {start:.1f}s à {end:.1f}s")

# Modification de la fonction STT pour inclure les segments des locuteurs
def start_stt_with_diarization():
    stt = SpeechToText("medium", output_audio_file, output_text_file)
    diarization = SpeakerDiarization(output_audio_file)
    segments = diarization.diarize()

    for start, end, speaker in segments:
        print(f"Transcription pour le locuteur {speaker} :")
        stt.start_for_segment(start, end)  # Transcrire uniquement le segment du locuteur

# Fichiers de sortie
AUDIOPATH = os.getenv("AUDIOPATH", "./")
TEXTPATH = os.getenv("TEXTPATH", "./")
output_audio_file = os.path.join(AUDIOPATH, "enregistrement_continue.wav")
output_text_file = os.path.join(TEXTPATH, "sortie.txt")

# Threads
recording_thread = threading.Thread(target=start_recording)
diarization_thread = threading.Thread(target=start_diarization)
stt_thread = threading.Thread(target=start_stt_with_diarization)

recording_thread.start()
diarization_thread.start()
stt_thread.start()

recording_thread.join()
diarization_thread.join()
stt_thread.join()

print("Enregistrement, diarisation et STT terminés.")

# # Fonction pour démarrer la reconnaissance vocale (STT)
# def start_stt():
#     stt = SpeechToText("medium", output_audio_file, output_text_file)
#     try:
#         stt.start()  # Cette méthode devrait traiter l'audio en continu
#     except KeyboardInterrupt:
#         print("Arrêt du traitement STT...")

# # Définition des chemins pour les fichiers audio et texte
# AUDIOPATH = os.getenv("AUDIOPATH", "./")
# TEXTPATH = os.getenv("TEXTPATH", "./")
# output_audio_file = os.path.join(AUDIOPATH, "enregistrement_continue.wav")
# output_text_file = os.path.join(TEXTPATH, "sortie.txt")

# # Création des threads pour l'enregistrement audio et le STT en simultané
# recording_thread = threading.Thread(target=start_recording)
# stt_thread = threading.Thread(target=start_stt)

# # Démarrage des deux threads
# recording_thread.start()
# stt_thread.start()

# # Attente de la fin des threads
# recording_thread.join()
# stt_thread.join()

# print("Enregistrement et STT terminés.")

########################################################################

# from recorder import SoundReceiverModule
# from stt import SpeechToText
# import time
# import os

# AUDIOPATH = os.getenv("AUDIOPATH", "./")
# TEXTPATH = os.getenv("TEXTPATH", "./")
# output_audio_file = os.path.join(AUDIOPATH, "enregistrement_continue.wav")
# output_text = os.path.join(TEXTPATH, "enregistrement_continue.raw")

# recorder = SoundReceiverModule(output_wav_file=output_audio_file,
#                                output_speech_detected_file=output_text,channel=1,#0,
#                                seconds_to_keep=15,
#                                sample_rate=44100 ,
#                                loudness_threshold=0.01)
# # recorder.start()
# try:
#     recorder.start()
# except KeyboardInterrupt:
#     print("Arrêt de l'enregistrement...")
#     recorder.stop()
    