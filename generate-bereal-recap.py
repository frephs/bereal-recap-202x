import os
import cv2
import numpy as np
import librosa
import moviepy.editor as mp
from tqdm import tqdm  # Importing tqdm for the progress bar

# Audio Analysis
audio_path = 'music.mp3'
y, sr = librosa.load(audio_path)
intensities = librosa.feature.rms(y=y)

# Image Processing
image_folder = 'bereal-export'
image_paths = sorted(os.listdir(image_folder))

frames = []
for img_path in tqdm(image_paths, desc='Loading Images'):  # Adding tqdm for image loading progress
    img = cv2.imread(os.path.join(image_folder, img_path))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
    frames.append(img)

# Cover Image
cover_frame = cv2.imread("bereal-cover/cover.png")
cover_frame = cv2.cvtColor(cover_frame, cv2.COLOR_BGR2RGB)

# Video Creation
output_video_path = 'output.mp4'

total_frames = len(frames)
audio_length = librosa.get_duration(y=y, sr=sr)

# Remap intensities to a scale of 0-3 based on quantiles
remapped_intensities = np.interp(intensities, (intensities.min(), intensities.max()), (0, 3))

# Function to calculate frame durations based on intensity levels
def get_frame_duration(t):
    idx = int(t * (intensities.shape[1] - 1) / audio_length)
    intensity_level = int(remapped_intensities[0, idx])
    return [0.5, 1.0, 1.5][intensity_level]

# Create a VideoClip with make_frame function and variable frame durations
cover_clip = mp.VideoClip(lambda t: cover_frame, duration=2)
video_clip = mp.VideoClip(lambda t: frames[int(t / audio_length * total_frames)], duration=audio_length)

# Calculate frame durations
frame_durations = [get_frame_duration(i / total_frames) for i in range(total_frames)]
frame_durations_sum = sum(frame_durations)

# Rescale frame durations to match audio length
rescale_factor = audio_length / frame_durations_sum
frame_durations = [duration * rescale_factor for duration in frame_durations]

# Set the durations for each frame
video_clip = video_clip.set_make_frame(lambda t: frames[int(t / audio_length * total_frames)])

# Set audio to middle clip
audio = mp.AudioFileClip(audio_path)
video_clip = video_clip.set_audio(audio)


# Concatenate cover clip, video clip, and cover clip
final_clip = mp.concatenate_videoclips([cover_clip, video_clip, cover_clip])

# Write video file
final_clip.write_videofile(output_video_path, codec='libx264', fps=30)

