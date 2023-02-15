from moviepy.editor import *

# Define the video parameters
duration = 10  # Duration of the video in seconds
fps = 25  # Frames per second
size = (640, 480)  # Frame size

# Create a function that generates the frames of the video
def make_frame(t):
    # Create a solid color frame
    color = (255, 0, 0)  # Red color
    frame = ImageClip(size)
    
    # Add a text message to the frame
    text = 'Hello, world!'
    text_clip = TextClip(text, fontsize=40, color='white').set_position('center')
    frame = CompositeVideoClip([frame, text_clip])
    
    return frame.get_frame(t)

# Create the video clip using the function that generates the frames
video_clip = VideoClip(make_frame, duration=duration)

# Write the video clip to a file
video_clip.write_videofile('output.mp4', fps=fps)
