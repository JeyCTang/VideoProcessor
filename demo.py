from moviepy.editor import VideoFileClip, vfx, AudioFileClip
import random

clip1 = VideoFileClip('./video_dir/2023-01-08 203739.mov', audio=False).subclip(0, 8)
# print(clip1.duration)

# audio1 = AudioFileClip('./video_dir/2023-01-08 203739.mov')
# audio1.write_audiofile('./output_dir/demoAU.mp3')

# clip1.audio = audio1

# new_clip = clip1.fx(vfx.time_mirror)
# new_clip = clip1.fx(vfx.mirror_x)
# new_clip = clip1.fx(vfx.fadeout, duration=1)
# new_clip = clip1.fx(vfx.invert_colors)
# new_clip = clip1.fx(vfx.rotate, angle=20)
# new_clip = clip1.add_mask().rotate(25)

ret = random.choices([1,2,3,4,5], k=3)
print(ret)
# new_clip = clip1.fx(vfx.speedx, factor=1.5)
# new_clip.write_videofile('./output_dir/demo5.mp4')