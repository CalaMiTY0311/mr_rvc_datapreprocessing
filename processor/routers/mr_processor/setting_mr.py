import os
import shutil
import zipfile 
import subprocess
from pydub import AudioSegment


class mr:
    def __init__(self, mr_dir, mr_id):
        self.mr_dir = mr_dir
        self.mr_id = mr_id

    def separating(self, stems, file):

        path = os.path.join(self.mr_dir,self.mr_id)
        os.makedirs(path, exist_ok=True)

        file.filename = file.filename.replace(" ", "_")
        if file.filename.lower().endswith('.wav'):
            file.filename = file.filename.split('.')[0] + '.mp3'
        file_path = os.path.join(path, file.filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        name, _ = os.path.splitext(file.filename)

        for song in os.listdir(path):
            if song == file.filename:
                spl = r'spleeter separate -p spleeter:' + \
                str(stems) + r'stems -o ' + os.path.join(path) + ' ' + os.path.join(path, name) + '.mp3'
                subprocess.run(spl, shell=True)
                os.remove(os.path.join(path, file.filename))

                make_zip = os.path.join(path, name)
                send_path = name + ".zip"
                send_path = os.path.join(path, send_path)
                print(make_zip,send_path)
                # print(path)
                shutil.make_archive(make_zip,'zip', make_zip)
                shutil.rmtree(make_zip)

        return send_path,path

        
    
    # 음원 합성
    def mix(self, file):

        path = os.path.join(self.mr_dir, self.mr_id)
        os.makedirs(path, exist_ok=True) 

        copy_path = os.path.join(path, file.filename)

        with open(copy_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        shutil.unpack_archive(copy_path, path, "zip")
        os.remove(copy_path)

        mrs = []
        for wavs in os.listdir(path):
            wavs = os.path.join(path, wavs)
            mrs.append(AudioSegment.from_wav(wavs))
            
        result_audio = mrs[0]
        for audio in mrs[1:]:
            result_audio = result_audio.overlay(audio)

        answer_file_name = "mixed_file.mp3"
        result_path = os.path.join(path,answer_file_name)
        result_audio.export(result_path, format="mp3")

        return result_path, path
