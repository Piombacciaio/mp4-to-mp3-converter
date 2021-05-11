from tkinter import Tk
import moviepy.editor
import os
from tkinter import *
from tkinter.filedialog import *

rt = Tk()
rt.geometry("500x110")
rt.title("MP4 to MP3 Converter")
rt.resizable(0,0)
rt.config(background="black")

path = "./converted"
access = 0o755
if not os.path.exists("converted"):
    os.mkdir(path, access)

vid = askopenfilename(filetypes=(("Video files", "*.mp4;*.flv;*.avi;*.mkv"), ("All files", "*.*") ))
name = os.path.basename(vid)[:-4]
vid = moviepy.editor.VideoFileClip(vid)
aud = vid.audio 
aud.write_audiofile(f"./converted/{name}-convert.mp3")  

print("Convert done")