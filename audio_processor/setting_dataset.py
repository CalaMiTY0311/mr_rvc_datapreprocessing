import librosa
import numpy as np
import os
import random, string
import soundfile as sf
import shutil

import zipfile

class data_processing:
    def __init__(self, dataset_dir, interval_seconds, wav_id):
        self.dataset_dir = dataset_dir
        self.interval_seconds = interval_seconds
        self.wav_id = wav_id

    def processing(self,file):
        
        wav_dir = os.path.join(self.dataset_dir, self.wav_id)
        os.makedirs(wav_dir, exist_ok=True)

        wav_path = os.path.join(wav_dir, file.filename)

        with open(wav_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        if file.filename.lower().endswith('.mp3') or file.filename.lower().endswith('.m4a'):
            path = os.path.join(wav_dir, file.filename)
            wav_path = os.path.splitext(path)[0] + '.wav'
            os.rename(path, wav_path)

        y, sr = librosa.load(wav_path, sr=22050, mono=True)
        for i, start in enumerate(range(0, len(y), self.interval_seconds * sr), 1):
            segment = y[start:start + self.interval_seconds * sr]
            output_file = os.path.join(wav_dir, f"dataset_{i - 1}.wav")
            sf.write(output_file, segment, sr, subtype='PCM_16')
        
        os.remove(wav_path)

        zip_path = os.path.join(wav_dir, 'dataset.zip')

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_name in os.listdir(wav_dir):
                if file_name.lower().endswith('.wav'):
                    file_path = os.path.join(wav_dir, file_name)
                    zipf.write(file_path, os.path.basename(file_path))
        
        for wav_file in os.listdir(wav_dir):
            if wav_file.endswith('.wav'):
                os.remove(os.path.join(wav_dir, wav_file))
        
        return zip_path
    





# def processing(self):

#         for wav_file in os.listdir(self.dataset_dir):

#             if wav_file.endswith('.wav'):
#                 wav_path = os.path.join(self.dataset_dir, wav_file)

#                 y, sr = librosa.load(wav_path, sr=22050, mono=True)

#                 for i, start in enumerate(range(0, len(y), self.interval_seconds * sr), 1):
#                     segment = y[start:start + self.interval_seconds * sr]
#                     output_file = os.path.join(self.dataset_dir, f"dataset_{i - 1}.wav")
#                     sf.write(output_file, segment, sr, subtype='PCM_16')

#         zip_name = 'dataset.zip'
#         zip_path = os.path.join(self.dataset_dir, zip_name)
#         with zipfile.ZipFile(zip_path, 'w') as zipf:
#             for wav_file in os.listdir(self.dataset_dir):
#                 if wav_file.endswith('.wav'):
#                     wav_path = os.path.join(self.dataset_dir, wav_file)
#                     zipf.write(wav_path, arcname=os.path.basename(wav_path))

#         return print("데이터를 성공적으로 분할하였습니다.")


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