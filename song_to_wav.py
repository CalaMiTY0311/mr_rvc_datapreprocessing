import librosa
import numpy as np
import os
import soundfile as sf

from pydub import AudioSegment

mp3_dir = 'mp3_dir' 
wav_dir = 'wav_dir' 

for filename in os.listdir(mp3_dir):
    if filename.endswith(".mp3"):
        mp3_path = os.path.join(mp3_dir, filename)
        print(mp3_path)
        
        track = AudioSegment.from_mp3(mp3_path)
        print(track)
        
        wav_path = os.path.join(wav_dir, f"{os.path.splitext(filename)[0]}.wav")
        file_handle = track.export(wav_path, format='wav')
        print(file_handle)


