import json

with open("video_links.json", "r") as f:
    data = json.load(f)

video_links = [f"https://www.youtube.com/watch?v={video['id']}" for video in data["entries"]]

# Save to a file
with open("video_links.txt", "w") as f:
    for link in video_links:
        f.write(link + "\n")
