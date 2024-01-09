import librosa
import numpy as np
import os
import soundfile as sf

wav = 'sud.wav'

(file_dir, file_id) = os.path.split(wav)

y,sr = librosa.load(wav,sr=16000)
output_directory = 'dataset'
interval_seconds = 15

y, sr = librosa.load(wav, sr=16000)

for i, start in enumerate(range(0, len(y), interval_seconds * sr), 1):
    segment = y[start:start + interval_seconds * sr]
    output_file = os.path.join(output_directory, f"recording_{i - 1}.wav")
    sf.write(output_file, segment, sr)