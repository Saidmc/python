from typing import Any
from pytube import YouTube

link = input("enter the youtube url: ")
yt = YouTube(link)
mp4files = yt.streams.filter(file_extension='mp4') #, progressive=True
print(type(mp4files))
video = list(enumerate(mp4files))

for i in video:
    print(i)

print("enter the desired option to download the format ")
dn_option = int(input(" enter the option: "))

dn_video = mp4files[dn_option]
dn_video.download()

print(" video was donwloaded successfully!! ")