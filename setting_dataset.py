import librosa
import numpy as np
import os
import soundfile as sf

def data_processing():

    input_dir = 'input_audio'               #input_audio 폴더에 자신의 목소리가 녹음 된 파일 넣기
    interval_seconds = 15                   #훈련 시키기 위해서 녹음 파일을 15초 마다 나눠야함
    output_dir = 'dataset'                  #나눈 데이터들은 dataset 폴더에 모여있으니까 이거 가지고 학습하면 됌

    os.makedirs(output_dir, exist_ok=True)

    for wav_file in os.listdir(input_dir):
        if wav_file.endswith('.wav'):
            wav_path = os.path.join(input_dir, wav_file)

            y, sr = librosa.load(wav_path, sr=22050, mono=True)

            for i, start in enumerate(range(0, len(y), interval_seconds * sr), 1):
                segment = y[start:start + interval_seconds * sr]
                output_file = os.path.join(output_dir, f"dataset_{i - 1}.wav")
                sf.write(output_file, segment, sr, subtype='PCM_16')
    return print('데이터 분리 완료')

