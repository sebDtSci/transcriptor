from pyannote.audio import Pipeline

class SpeakerDiarization:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    def diarize(self):
        diarization = self.pipeline({"uri": self.audio_file, "audio": self.audio_file})
        segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append((turn.start, turn.end, speaker))
        return segments