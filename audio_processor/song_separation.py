import os
import shutil

from fastapi import APIRouter
router = APIRouter()


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

def separation(stems, file_name):

    path = 'song_dir'
    os.chdir(path)
    nsfile_name = file_name.replace(' ', '_')

    try:
        os.rename(path+file_name+'.mp3', path+nsfile_name+'.mp3') 
    except FileNotFoundError:
        pass
    print('기다려주세요.')

    output_directory = os.path.join('separation_output', nsfile_name)

    # output 폴더의 HeartAttack 디렉토리 비우기
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)

    spl = r'spleeter separate -p spleeter:' + \
        str(stems)+r'stems -o output '+nsfile_name+'.mp3'
    # 'spleeter separate -p spleeter:2stems -o output my_song.mp3'
    os.system(spl)
    
    return print('분리 완료')


