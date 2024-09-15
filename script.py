import os
from pathlib import Path
atual=os.getcwd()
arquivos=list(Path(atual).glob('*mp4'))
i=1
if (len(arquivos)==0):
    print('Não existem arquivos')
else:
    for arq in arquivos:
        if 'E01' in str(arq):
            a=str(arq)
            a=a.split('\\')
            ext1='mp4'
            ext2='srt'
            arquivos=list(Path(atual).glob('*srt'))
            break
        else:
            arquivos=list(Path(atual).glob('*srt'))
    for arq in arquivos:
        if 'E01' in str(arq):
            a=str(arq)
            a=a.split('\\')
            ext1='srt'
            ext2='mp4'
            arquivos=list(Path(atual).glob('*mp4'))
            break
for x in a:
    if 'mp4' in x:
        a=x
    elif 'srt' in x:
        a=x        
for arq in arquivos:
    titulo=a.replace('E01',f'E{str(i).zfill(2)}')
    titulo=titulo.replace(ext1,ext2)
    os.rename(arq,titulo)
    i+=1