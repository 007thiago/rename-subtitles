import os
from pathlib import Path
current=os.getcwd()
video_format=input('Formato de vídeo: ')
files=list(Path(current).glob('*srt'))
i=1
if (len(files)==0):
    print('Não existem arquivos.')
else:
    if 'E01' in str(files[0]):
        a=str(files[0]).split('\\')
        ext1='srt'
        ext2=video_format
        files=list(Path(current).glob(f'*{video_format}'))
    else:
        files=list(Path(current).glob(f'*{video_format}'))
        if 'E01' in str(files[0]):
            a=str(files[0]).split('\\')
            ext1=video_format
            ext2='srt'
            files=list(Path(current).glob('*srt'))
a=a[len(a)-1]
for file in files:
    title=a.replace('E01',f'E{str(i).zfill(2)}')
    title=title.replace(ext1,ext2)
    os.rename(file,title)
    i+=1