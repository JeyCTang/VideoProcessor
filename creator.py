import os
from moviepy.editor import VideoFileClip, vfx, AudioFileClip
import random
import time

class Creator:
    def __init__(self, save_dir, out_dir) -> None:
        self.save_dir = save_dir
        self.out_dir = out_dir
        self.video_lst = self.get_videos_list()

    # Get the filenames of video in the input directory
    def get_videos_list(self) -> list:
        abs_path = os.path.abspath('.')
        video_names = os.listdir(f'{self.save_dir}')
        return [os.path.join(abs_path, self.save_dir, video) for video in video_names]

    # Choose three methods to re-process the video, each time the process method is different
    
    # Change the video to black and white
    def ch_bw(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.blackwhite)
    
    # Get the mirror-x of the video
    def ch_mirX(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.mirror_x)

    # Change the brightness
    def ch_brit(self, v_file: VideoFileClip) -> VideoFileClip:
        fac = random.uniform(0.8, 1.2)
        return v_file.fx(vfx.colorx, factor=fac)
    
    # Play backwards
    def bk_play(self, v_file: VideoFileClip) -> VideoFileClip:
        du = v_file.duration
        v_clip = v_file.subclip(0, int(du))
        return v_clip.fx(vfx.time_mirror)

    # add fadeout effect
    def fade_out(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.fadeout, duration=1)
    
    # reverse the color
    def rev_clor(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.invert_colors)
    
    # speed up or down the video
    def speed_v(self, v_file: VideoFileClip) -> VideoFileClip:
        fac = random.uniform(0.9, 1.1)
        return v_file.fx(vfx.speedx, factor=fac)

    # slightly resize the video
    def resize_v(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.resize, new_size = random.uniform(0.95, 1.05))

    # slightly rotate the video
    def rotate_v(self, v_file: VideoFileClip) -> VideoFileClip:
        return v_file.fx(vfx.rotate, angle=random.randint(-5, 5))
    
    # sample the processing methods, each time we use four
    def sample_methods(self) -> list:
        methods_dict = {
            0: self.ch_bw,
            1: self.ch_mirX,
            2: self.ch_brit,
            3: self.bk_play,
            4: self.fade_out,
            5: self.rev_clor,
            6: self.speed_v,
            7: self.resize_v,
            8: self.rotate_v
        }
        choosed_mth = random.sample([1, 2, 3, 4, 6], k = 3)
        print(choosed_mth)
        return [methods_dict[i] for i in choosed_mth]

    def process_video(self) -> None:
        for video in self.video_lst:
            methods = self.sample_methods()
            v_clip = VideoFileClip(video, audio=False)
            a_clip = AudioFileClip(video)
            for method in methods:
                v_clip = method(v_clip)
            v_clip = v_clip.set_audio(a_clip)
            v_clip.write_videofile(os.path.join(self.out_dir, f'{time.time()}_result.mp4'))

            # close the v_clip and a_clip after writing down the processed clip
            a_clip.close()
            v_clip.close()
    


if __name__=='__main__':
    creator = Creator(save_dir='./video_dir', out_dir='./output_dir')
    creator.process_video()
