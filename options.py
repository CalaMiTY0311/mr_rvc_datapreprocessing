# export PATH=$PATH:/c/Users/axels/OneDrive/바탕\ 화면/translation_AI/ffmpeg-6.1.1-full_build/bin

import os 

from setting_dataset import data_processing
from song_separation import separation


options = int(input('options 선택'))
# options 1 : data_processing
# options 2 : song_separation
# options 3 : 1,2 one-shot setting

def process_music(stems_prompt='stems 선택 : 2, 4, 5 >>>', name_prompt='음악 파일의 이름을 적어주세요. >>>'):
    stems = str(input(stems_prompt))
    file_name = str(input(name_prompt))
    return stems, file_name

if options==1:
    data_processing()
elif options==2:
    stems, file_name = process_music()
    separation(stems, file_name)
elif options==3:
    data_processing()
    stems, file_name = process_music()
    separation(stems, file_name)
else:
    print('Options 1,2,3중에서 골라주세요')