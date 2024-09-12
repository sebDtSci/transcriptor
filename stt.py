# stt.py

import os
from faster_whisper import WhisperModel
import time
import logging
from dotenv import load_dotenv

class SpeechToText:

    def __init__(self, model_path:str="medium", input_audio_path:str=None, output_file:str=None):
        self.model = WhisperModel(model_path)
        self.input_audio = input_audio_path
        self.output_file = output_file
        self.transcribtion = ""
    
    def _write(self):
        with open(self.output_file, 'a') as f: # a et pas w
            # f.write(self.transcribtion)
            f.write(self.transcribtion + '\n')

    def start(self):
        if not os.path.isfile(self.input_audio):
            raise FileNotFoundError(f"The file {self.input_audio} does not exist or is not readable.")
        
        self.running = True
        all_transcriptions = []  # Liste pour stocker toutes les transcriptions


        while self.running:
            try:
                segments, info = self.model.transcribe(self.input_audio)
                text = " ".join([segment.text for segment in segments])
                # all_transcriptions.append(text)  # Ajouter chaque nouvelle transcription
                self.transcribtion = text
                self._write()
                # time.sleep(0.1)
            except Exception as e:
                logging.error(f"Transcription failed: {e}")
        # transcribtion_final = "\n".join(all_transcriptions)
        # print(transcribtion_final)
        # self.transcribtion = transcribtion_final
        # self._write()
    
if __name__ == "__main__":
    load_dotenv()

    AUDIOPATH = os.getenv("AUDIOPATHW", "./")
    TEXTPATH = os.getenv("TEXTPATHW", "./")
    output_audio_file = os.path.join(AUDIOPATH,"enregistrement_continue.wav")#"common_voice_fr_40187663.mp3")# "enregistrement_continue.wav")
    output_text = os.path.join(TEXTPATH, "sortie.txt")
    
    
    stt = SpeechToText("medium", output_audio_file, output_text)
    stt.start()