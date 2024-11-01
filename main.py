import os
from pathlib import Path
current=os.getcwd()

#Function to rename all files (in case there is no sequencial title on the files), starting with subtitles
def renameAll(files1, files2, files3, subs,video):
    """ Rename all files with a newly created string representing a sequential title. """
    i=1
    a=str(files1[0]).split('\\')
    a='E01_' + a[-1]
    for file in files3:
        #If all subtitles files are already renamed,
        #then counter resets in order to iterate through video files (based on the amount of sub files)
        if (i==(s+1)):
            i=1
            ext1=subs
            ext2=video
            a=a.replace(ext1,ext2)
        title=a.replace('E01_',f'E{str(i).zfill(2)}_')
        os.rename(file,title)
        i+=1
        
#Function to rename only subs/videos (in case there is a sequencial title on videos/subs)
def renameSome(files1, files2, files3, subs, video):
    """ Rename only subtitle or video files depending on which one has a sequential title. """
    i=1
    if ('E01' in str(files1[0])):
        a=str(files1[0]).split('\\')
        files=files2
        ext1,ext2=subs,video
    else:
        a=str(files2[0]).split('\\')
        files=files1
        ext1,ext2=video,subs
        i=1
    a=a[len(a)-1]
    for file in files:
        title=a.replace(ext1,ext2)
        title=title.replace('E01',f'E{str(i).zfill(2)}')
        os.rename(file,title)
        i+=1

videoF,subF=input('Video format: '),input('Subtitle format: ')
files1,files2=list(Path(current).glob(f'*{subF}')),list(Path(current).glob(f'*{videoF}'))
files3=(files1+files2)
s=len(files1)
i=1

if (len(files1)==0) or (len(files2)==0):
    print('There\'re no video/subtitle files.')
else:
    if ('E01' not in str(files1[0])) and ('E01' not in str(files2[0])): #If there isn't a default rule
        #on videos/subtitles titles, one will be created
        renameAll(files1, files2, files3, subF,videoF)
    else:
        renameSome(files1, files2, files3, subF, videoF)