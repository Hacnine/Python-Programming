# Python code to convert video to audio 
import moviepy.editor as mp

# Insert Local Video File Path  
clip = mp.VideoFileClip(r"audio_video_editor/Surah-Yasin")

# Insert Local Audio File Path
clip.audio.write_audiofile(r"Audio File")
