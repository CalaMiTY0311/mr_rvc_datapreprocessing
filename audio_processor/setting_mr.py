import os
import shutil
import zipfile 
import subprocess


class mr:
    def __init__(self, mr_dir, mr_id):
        self.mr_dir = mr_dir
        self.mr_id = mr_id

    def separating(self, stems, file):

        path = os.path.join(self.mr_dir)
        
        save_song = os.path.join(path, file.filename)
        with open(save_song, "wb") as f:
            shutil.copyfileobj(file.file, f)
        get_file = file.filename
        name, _ = os.path.splitext(get_file)

        for song in os.listdir(path):
            if song == get_file:
                spl = r'spleeter separate -p spleeter:' + \
                str(stems) + r'stems -o ' + os.path.join(path, self.mr_id) + ' ' + os.path.join(path, name) + '.mp3'
                flag = subprocess.run(spl, shell=True)
                os.remove(os.path.join(path, get_file))

        zip_name = f'{stems}_{name}.zip'
        zip_path = os.path.join(path, self.mr_id, name, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            result_path = os.path.join(self.mr_dir, self.mr_id, name)
            for files in os.listdir(result_path):
                if files.lower().endswith('.wav'):
                    result = os.path.join(result_path, files)
                    zipf.write(result, os.path.basename(result))
        
        delete_path = os.path.join(path, self.mr_id)
        
        return zip_path, zip_name, delete_path                    
    