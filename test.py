import librosa
import numpy as np
import os
import soundfile as sf

input_dir = 'input_audio'
output_dir = 'dataset'
interval_seconds = 15

os.makedirs(output_dir, exist_ok=True)

for wav_file in os.listdir(input_dir):
    if wav_file.endswith('.wav'):
        wav_path = os.path.join(input_dir, wav_file)

        y, sr = librosa.load(wav_path, sr=44100, mono=True)

        for i, start in enumerate(range(0, len(y), interval_seconds * sr), 1):
            segment = y[start:start + interval_seconds * sr]
            output_file = os.path.join(output_dir, f"dataset_{i - 1}.wav")
            sf.write(output_file, segment, sr, subtype='PCM_16')