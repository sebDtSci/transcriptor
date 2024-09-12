from pyannote.audio import Pipeline
from faster_whisper import WhisperModel
import os

Token = os.getenv("Token")

# Charger le modèle de diarization pyannote
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=Tokenb)

# Charger un fichier audio
audio_file = "path_to_audio_file.wav"

# Effectuer la diarization pour détecter les locuteurs
diarization = pipeline(audio_file)

# Charger le modèle Whisper
model = WhisperModel("base")

# Transcrire l'audio avec Whisper
segments, info = model.transcribe(audio_file)

# Associer la transcription aux segments de diarization
for segment in diarization.itertracks(yield_label=True):
    start_time, end_time = segment[0].start, segment[0].end
    speaker = segment[1]

    # Extraire la transcription pour le segment
    for s in segments:
        if start_time <= s.start < end_time:
            print(f"Speaker {speaker}: {s.text}")
