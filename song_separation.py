import os

# 2stems = 보컬 + 배경 음악
# 4stems = 보컬 + 드럼 + 베이스 + 나머지
# 5stems = 보컬 + 드럼 + 베이스 + 피아노 + 나머지
stems = 2
path = 'song_dir'
os.chdir(path)

file_name = ''                                  # <------------------ 노래(Lemon.mp3 라면 Lemon만 치셈)

nsfile_name = file_name.replace(' ', '_')

try:
    os.rename(path+file_name+'.mp3', path+nsfile_name+'.mp3')
except FileNotFoundError:
    pass
print('기다려주세요.')
spl = r'spleeter separate -p spleeter:' + \
    str(stems)+r'stems -o output '+nsfile_name+'.mp3'
# 'spleeter separate -p spleeter:2stems -o output my_song.mp3'
os.system(spl)




# import shutil
# pretrained_models_path = os.path.join(path, 'pretrained_models')
# if os.path.exists(pretrained_models_path):
#     shutil.rmtree(pretrained_models_path)
#     print('pretrained_models 디렉토리 삭제 완료.')
# else:
#     print('pretrained_models 디렉토리가 이미 존재하지 않습니다.')