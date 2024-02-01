import os
import shutil
import zipfile 
import subprocess


class mr:
    def __init__(self, mr_dir, mr_id, stems):
        self.mr_dir = mr_dir
        self.mr_id = mr_id
        self.stems = stems

    def separating(self, file):

        path = os.path.join(self.mr_dir)
        
        save_song = os.path.join(path, file.filename)
        with open(save_song, "wb") as f:
            shutil.copyfileobj(file.file, f)
        get_file = file.filename
        name, _ = os.path.splitext(get_file)

        for song in os.listdir(path):
            if song == get_file:
                spl = r'spleeter separate -p spleeter:' + \
                str(self.stems) + r'stems -o ' + os.path.join(path, self.mr_id) + ' ' + os.path.join(path, name) + '.mp3'
                flag = subprocess.run(spl, shell=True)
                os.remove(os.path.join(path, get_file))

        zip_name = f'{self.stems}_{name}.zip'
        zip_path = os.path.join(path, self.mr_id, name, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            result_path = os.path.join(self.mr_dir, self.mr_id, name)
            for files in os.listdir(result_path):
                if files.lower().endswith('.wav'):
                    result = os.path.join(result_path, files)
                    zipf.write(result, os.path.basename(result))
        
        return zip_path                    
    

        # return zip_path
    # def separating(self, file):
    #     mr_dir = os.path.join(self.mr_dir, self.mr_id)
    #     os.makedirs(mr_dir, exist_ok=True)

    #     path = os.path.join(mr_dir, file.filename)

    #     with open(path, "wb") as f:
    #         shutil.copyfileobj(file.file, f)
    
    #     if file.filename.endswith('.wav') or file.filename.endswith('.m4a'):
    #         path = os.path.join(mr_dir, file.filename)
    #         mp3_path = os.path.splitext(path)[0] + '.mp3'
    #         os.rename(path, mp3_path)
        
    #     print(mp3_path)

    #     return path
        
        


        
        

        

# def separation(stems, file_name):

#     path = 'song_dir'
#     os.chdir(path)
#     nsfile_name = file_name.replace(' ', '_')

#     try:
#         os.rename(path+file_name+'.mp3', path+nsfile_name+'.mp3') 
#     except FileNotFoundError:
#         pass
#     print('기다려주세요.')

#     output_directory = os.path.join('separation_output', nsfile_name)

#     # output 폴더의 HeartAttack 디렉토리 비우기
#     if os.path.exists(output_directory):
#         shutil.rmtree(output_directory)

#     spl = r'spleeter separate -p spleeter:' + \
#         str(stems)+r'stems -o output '+nsfile_name+'.mp3'
#     # 'spleeter separate -p spleeter:2stems -o output my_song.mp3'
#     os.system(spl)
    
#     return print('분리 완료')
