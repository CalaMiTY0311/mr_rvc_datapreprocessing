import librosa
import os
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

        if file.filename.lower().endswith('.mp3'):
            file.filename = file.filename.split('.')[0] + '.wav'
            
        file_path = os.path.join(path, file.filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        y, sr = librosa.load(file_path, sr=self.hz[0], mono=True)
        for i, start in enumerate(range(0, len(y), self.interval_seconds[0] * sr), 1):
            segment = y[start:start + self.interval_seconds[0] * sr]
            output_file = os.path.join(path, f"dataset_{i - 1}.wav")
            sf.write(output_file, segment, sr, subtype='PCM_16')
        
        os.remove(file_path)
        zip_path = os.path.join(path, 'dataset.zip')
        print(zip_path)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for wavs in os.listdir(path):
                if wavs.lower().endswith('.wav'):
                    result_path = os.path.join(path, wavs)
                    zipf.write(result_path, os.path.basename(result_path))
        
        return zip_path, path
