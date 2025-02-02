from moviepy.editor import *
import os
from moviepy import editor
from pydub import AudioSegment
import sys
import multiprocessing

def create_video(i, username, images_folder, abs_path):
    audio_seg_path = os.path.join(f"src/audio/{username}/seg_{i}.mp3")
    sound = AudioSegment.from_file(audio_seg_path)
    image_clip = ImageClip(os.path.join(images_folder, images[i])).set_duration(sound.duration_seconds)
    audio_clip = AudioFileClip(audio_seg_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.write_videofile(os.path.join(abs_path, f"src/video/{username}/seg_{i}.mp4"), threads=8, fps=24)

abs_path = "/home/kunj/freelance_prj/text_to_video/web_app/Web_VideoAI/VideoAI/static"
os.chdir(abs_path)
username = sys.argv[1]
images_folder = os.path.join(f'src/images/{username}')
images = [image for image in os.listdir(images_folder)]
images.sort()
pool = multiprocessing.Pool()
for i in range(len(images)):
        pool.apply_async(create_video, args=(i, username, images_folder, abs_path))
pool.close()
pool.join()

final_video = concatenate_videoclips([VideoFileClip(os.path.join(abs_path, f"src/video/{username}/seg_{i}.mp4")) for i in range(0, len(images))])
final_video.write_videofile(os.path.join(abs_path, f"src/video/{username}/Final_video.mp4"), threads = 8 , fps=24)
