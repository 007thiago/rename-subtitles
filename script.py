import os
from pathlib import Path
current=os.getcwd()
videoF=input('Video format: ')
subF=input('Subtitle format: ')
files1=list(Path(current).glob(f'*{subF}'))
files2=list(Path(current).glob(f'*{videoF}'))
files3=files1+files2
s=len(files1)
i=1
if (len(files1)==0) or (len(files2)==0):
    print('There\'re no video/subtitle files.')
else:
    #If there isn't a default rule on videos/subtitles titles, one will be created
    if ('E01' not in str(files1[0])) and ('E01' not in str(files2[0])):
        a=str(files1[0]).split('\\')
        a='E01_' + a[len(a)-1]
        for file in files3:
            #If all subtitles files are already renamed, then counter resets in order to iterate through video files, and the source extension is now subtitle (subtitle -> video file)
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
            a=str(files1[0]).split('\\')
            files=files2
            ext1,ext2=subF,videoF
        else:
            a=str(files2[0]).split('\\')
            files=files1
            ext1,ext2=videoF,subF
        a=a[len(a)-1]
        i=1
        for file in files:
            title=a.replace(ext1,ext2)
            title=title.replace('E01',f'E{str(i).zfill(2)}')
            os.rename(file,title)
            i+=1