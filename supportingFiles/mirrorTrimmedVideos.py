import os
import subprocess

# Directories
input_dir = "regular_kickflip_videos"  # Directory containing the trimmed videos
output_dir = "goofy_kickflip_videos"  # Directory to save mirrored videos
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# List all files in the input directory
video_files = [f for f in os.listdir(input_dir) if f.endswith(('.avi', '.mp4', '.mkv'))]

# Process each video file
for video_file in video_files:
    input_video = os.path.join(input_dir, video_file)
    output_video = os.path.join(output_dir, f"mirrored_{video_file}")

    # FFmpeg command to mirror the video (flip horizontally)
    command = [
        "ffmpeg",
        "-i", input_video,        # Input video
        "-vf", "hflip",           # Horizontal flip filter
        "-c:a", "copy",           # Copy audio codec
        output_video              # Output video
    ]

    # Execute the FFmpeg command
    try:
        subprocess.run(command, check=True)
        print(f"Mirrored video saved as {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error mirroring {video_file}: {e}")
