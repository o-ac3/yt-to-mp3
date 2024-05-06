import time, os
from tqdm import tqdm
from pydub import AudioSegment
from pytube import YouTube
from tkinter.filedialog import *



filename = askopenfile( initialdir="C:/", title="select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")) )

music_dir = os.path.expanduser("~/Music/mp3/")
filetype = ".mp3"

if not os.path.exists(music_dir):
    os.makedirs(music_dir)

with open(filename.name) as file:
    items=file.readlines()

    for item in items: 
        yt = YouTube(item)
        yt_audio = yt.streams.get_audio_only()
        yt_file = yt_audio.download(music_dir)
       
for files in os.listdir(music_dir):
    
    file_path = os.path.join(music_dir, files)

    if files.endswith(".mp4"):
        base, ext = os.path.splitext(files)
        new_filename = os.path.join(music_dir, base + filetype)
        music_file = os.rename(file_path, new_filename)
        print(str(base) + ' download successfully')

print('---DOWNLOAD COMPLETE---')

