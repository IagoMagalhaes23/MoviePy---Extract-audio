from moviepy.editor import *
from pathlib import Path

def extract_audio(path_list):
    for file in path_list:
        videoclip = VideoFileClip(str(file))
        videoclip.audio.write_audiofile(f"{str(file)}.mp3")

directory_to_save = r"MoviePy - Extract audio/arquivos"
path_list = Path(directory_to_save).glob("*.mp4")

audio_mp3 = extract_audio(path_list)