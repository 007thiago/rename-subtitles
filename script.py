import os
from pathlib import Path
current=os.getcwd()
video_format=input('Formato de vídeo: ')
files=list(Path(current).glob(f'*.{video_format}'))
i=1
if (len(files)==0):
    print('Não existem arquivos')
else:
    for file in files:
        if 'E01' in str(file):
            a=str(file)
            a=a.split('\\')
            ext1='mp4'
            ext2='srt'
            files=list(Path(current).glob('*srt'))
            break
        else:
            files=list(Path(current).glob('*srt'))
    for file in files:
        if 'E01' in str(file):
            a=str(file)
            a=a.split('\\')
            ext1='srt'
            ext2='mp4'
            files=list(Path(current).glob(f'*.{video_format}'))
            break
for x in a:
    if (f'{video_format}') in x:
        a=x
    elif 'srt' in x:
        a=x        
for file in files:
    title=a.replace('E01',f'E{str(i).zfill(2)}')
    title=title.replace(ext1,ext2)
    os.rename(file,title)
    i+=1