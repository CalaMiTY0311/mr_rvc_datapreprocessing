import librosa
import numpy as np
import os
import soundfile as sf
from pydub import AudioSegment

import zipfile

class data_processing:
    def __init__(self, dataset_dir, interval_seconds):
        self.dataset_dir = dataset_dir
        self.interval_seconds = interval_seconds

    def processing(self):

        for wav_file in os.listdir(self.dataset_dir):

            if wav_file.endswith('.wav'):
                wav_path = os.path.join(self.dataset_dir, wav_file)

                y, sr = librosa.load(wav_path, sr=22050, mono=True)

                for i, start in enumerate(range(0, len(y), self.interval_seconds * sr), 1):
                    segment = y[start:start + self.interval_seconds * sr]
                    output_file = os.path.join(self.dataset_dir, f"dataset_{i - 1}.wav")
                    sf.write(output_file, segment, sr, subtype='PCM_16')

        zip_name = 'dataset.zip'
        zip_path = os.path.join(self.dataset_dir, zip_name)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for wav_file in os.listdir(self.dataset_dir):
                if wav_file.endswith('.wav'):
                    wav_path = os.path.join(self.dataset_dir, wav_file)
                    zipf.write(wav_path, arcname=os.path.basename(wav_path))

        return print("데이터를 성공적으로 분할하였습니다.")

# from pydub import AudioSegment
# mp3_file = 'bbb.mp3' 
# wav_filename = 'bbb.wav' 
# track = AudioSegment.from_mp3(mp3_file)
# print(track)
# file_handle = track.export(wav_filename, format='wav')
# print(file_handle)

#  

# 소스2 : m4aToWav.py
#  


# from pydub import AudioSegment
# m4a_file = 'aa.m4a'
# wav_filename = 'aa.wav'
# track = AudioSegment.from_file(m4a_file,  format= 'm4a')
# file_handle = track.export(wav_filename, format='wav')
# 출처: https://pagichacha.tistory.com/141 [파기차차:티스토리]