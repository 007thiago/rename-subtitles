import os
from pathlib import Path
current=os.getcwd()
videoF=input('Formato de vídeo: ')
subF=input('Formato de legenda: ')
files1=list(Path(current).glob(f'*{subF}'))
files2=list(Path(current).glob(f'*{videoF}'))
files3=files1+files2
s=len(files1)
i=1
if (len(files1)==0) or (len(files2)==0):
    print('Não existem arquivos de vídeo/legenda.')
else:
    if ('E01' not in str(files1[0])) and ('E01' not in str(files2[0])):
        a=str(files1[0]).split('\\')
        a='E01_' + a[len(a)-1]
        for file in files3:
            if (i==(s+1)):
                i=1
                ext1=subF
                ext2=videoF
                a=a.replace(ext1,ext2)
            title=a.replace('E01_',f'E{str(i).zfill(2)}_')
            os.rename(file,title)
            i+=1
    else:
        if ('E01' in str(files1[0])):
            ext1=subF
            ext2=videoF
            files=files2
            a=str(files1[0]).split('\\')
        else:
            ext1=videoF
            ext2=subF
            files=files1
            a=str(files2[0]).split('\\')
        a=a[len(a)-1]
        i=1
        for file in files:
            title=a.replace('E01',f'E{str(i).zfill(2)}')
            title=title.replace(ext1,ext2)
            os.rename(file,title)
            i+=1