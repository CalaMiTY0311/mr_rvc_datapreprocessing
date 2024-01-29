import os
import shutil

# stems = 4
# path = 'song_dir'                                           # 배경 음악을 제거할려면 song_dir에 노래를 넣어 (mp3로)
# os.chdir(path) 

# file_name = 'HeartAttack'                                   # <------------------ 노래(Lemon.mp3 라면 Lemon만 치셈)

# nsfile_name = file_name.replace(' ', '_')

# try:
#     os.rename(path + file_name + '.mp3', path + nsfile_name + '.mp3') 
# except FileNotFoundError:
#     pass

# print('기다려주세요.')

# output_directory = os.path.join('output', nsfile_name)

# # output 폴더의 HeartAttack 디렉토리 비우기
# if os.path.exists(output_directory):
#     shutil.rmtree(output_directory)

# spl = r'spleeter separate -p spleeter:' + \
#     str(stems) + r'stems -o output ' + nsfile_name + '.mp3'
# # 'spleeter separate -p spleeter:2stems -o output my_song.mp3'
# os.system(spl)
# print('분리 완료')

class mr:
    def __init__(self, mr_dir, mr_id, stems):
        self.mr_dir = mr_dir
        self.mr_id = mr_id
        self.stems = stems

    def separating(self, file):
        mr_dir = os.path.join(self.mr_dir, self.mr_id)
        os.makedirs(mr_dir, exist_ok=True)

        path = os.path.join(mr_dir, file.filename)

        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        return path        
        # if file.filename.endswith('.wav') or file.filename.endswith('.m4a'):
        #     path = os.path.join(separation_dir, file.filename)
        #     mp3_path = os.path.splitext(path)[0] + '.mp3'
        #     os.rename(path, mp3_path)
        
        


        
        

        

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
