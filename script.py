import os
from pathlib import Path
current=os.getcwd()
video_format=input('Formato de vídeo: ')
files1=list(Path(current).glob(f'*.{video_format}'))
files2=files=list(Path(current).glob('*srt'))
i=1
if (len(files)==0):
    print('Não existem arquivos.')
else:
    a=str(files1[0]).split('\\')
    a=a[len(a)-1]
    if 'E01' in str(files1[0]):
        ext1=video_format
        ext2='srt'
    elif 'E01' in str(files2[0]):
        ext1='srt'
        ext2=video_format
    else:
        print('Não existe padrão sequencial nos títulos.')
for file in files:
    title=a.replace('E01',f'E{str(i).zfill(2)}')
    title=title.replace(ext1,ext2)
    os.rename(file,title)
    i+=1