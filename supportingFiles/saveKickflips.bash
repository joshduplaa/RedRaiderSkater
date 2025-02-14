#!/bin/bash

# Create the output folder if it doesn't exist
mkdir -p kickflip_videos

# Initialize counter
kickCount=0

# Path to the text file containing video links
linksFile="video_links.txt"

# Loop through each link in the text file
while IFS= read -r link; do
  # Increment the counter
  kickCount=$((kickCount + 1))

  # Download and convert video to .avi
  yt-dlp -f best -o "kickflip_videos/${kickCount}_kickflip.avi" --recode-video avi "$link"
done < "$linksFile"

echo "All videos have been downloaded and stored in the 'kickflip_videos' folder."
