import os
# 2stems = 보컬 + 배경 음악
# 4stems = 보컬 + 드럼 + 베이스 + 나머지
# 5stems = 보컬 + 드럼 + 베이스 + 피아노 + 나머지

stems = str(input('stems 선택 : 2, 4, 5 >>>'))

path = str(input(r'파일이 있는 경로를 정해주세요. >>>'))
os.chdir(path)
file_name = str(input('음악 파일의 이름을 적어주세요. >>>'))

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