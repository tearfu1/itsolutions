from moviepy.editor import TextClip, CompositeVideoClip

def create_text_video(text, output_file='output.mp4'):
    width, height = 100, 100
    duration = 3

    text_clip = TextClip(text, fontsize=100, color='white', font='Bookman-Demi')

    start_x = width
    end_x = -text_clip.w

    text_clip = text_clip.set_position(lambda t: (start_x + t * (end_x - start_x) / duration, 'center'))
    text_clip = text_clip.set_duration(duration)

    final_clip = CompositeVideoClip([text_clip], size=(width, height), bg_color=(100,100,100))
    final_clip.write_videofile(output_file, fps=24)
