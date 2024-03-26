import librosa
import numpy as np
import os
import random, string
import soundfile as sf
import shutil

import zipfile

class data_processing:
    def __init__(self, dataset_dir, interval_seconds, hz, wav_id):
        self.dataset_dir = dataset_dir
        self.interval_seconds = interval_seconds,
        self.hz = hz,
        self.wav_id = wav_id

    def processing(self,file):

        path = os.path.join(self.dataset_dir, self.wav_id)
        os.makedirs(path, exist_ok=True)

        if file.filename.lower().endswith('.mp3') or file.filename.lower().endswith('.m4a'):
            file.filename = file.filename.split('.')[0] + '.wav'
            
        file_path = os.path.join(path, file.filename)
        print(file_path, file.filename, file)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # 사용자로 부터 받은 interval_second 단위(초)로 wav에 hz 값을 반영
        y, sr = librosa.load(file_path, sr=self.hz[0], mono=True)
        for i, start in enumerate(range(0, len(y), self.interval_seconds[0] * sr), 1):
            segment = y[start:start + self.interval_seconds[0] * sr]
            output_file = os.path.join(path, f"dataset_{i - 1}.wav")
            sf.write(output_file, segment, sr, subtype='PCM_16')
        
        os.remove(file_path)
        zip_path = os.path.join(path, 'dataset.zip')

        # interval_second 단위로 쪼갠 wav파일들을 zip으로 압축시킴
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_name in os.listdir(path):
                if file_name.lower().endswith('.wav'):
                    result_path = os.path.join(path, file_name)
                    zipf.write(result_path, os.path.basename(result_path))
        
        
        for wav_file in os.listdir(path):
            if wav_file.endswith('.wav'):
                os.remove(os.path.join(path, wav_file))
        
        return zip_path, path
