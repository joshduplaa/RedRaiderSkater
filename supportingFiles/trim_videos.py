import os
import subprocess

# Directories
input_dir = "kickflip_videos"  # Directory containing the original videos
output_dir = "regular_kickflip_videos"  # Directory to save trimmed videos
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# Dictionary containing video identifiers and time ranges
relevantkickfliptimes = {
    332: (32, 37),
    331: (9, 14),
    330: (11, 15),
    329: (13, 16),
    328: (3, 6),
    327: (3, 6),
    326: (4, 7),
    325: (3, 7),
    324: (8, 11),
    323: (3, 5),
    322: (3, 6),
    321: (7, 10),
    320: (7, 10),
    319: (10, 13),
    318: (18, 21),
    317: (1, 3),
    316: (15, 18),
    315: (4, 7),
    314: (2, 6),
    313: (2, 6),
    312: (3, 7),
    311: (9, 12),
    310: (2, 6),
    309: (1, 5),
    308: (14, 19),
    307: (6, 11),
    306: (3, 7),
    305: (5, 9),
    304: (3, 7),
    303: (2, 6),
    302: (14, 20),
    301: (18, 21),
    300: (2, 6),
    299: (3, 8),
    298: (4, 8),
    297: (3, 6),
    296: (5, 10),
    295: (2, 6),
    294: (6, 10),
    293: (12, 17),
    292: (3, 6),
    291: (10, 15),
    290: (2, 6),
    289: (4, 7),
    288: (7, 11),
    287: (3, 8),
    286: (5, 9),
    285: (4, 7),
    284: (11, 15),
    283: (22, 26),
    282: (9, 13),
    281: (4, 8),
    280: (4, 8),
    279: (4, 8),
    278: (2, 6),
    277: (6, 10),
    276: (4, 7),
    275: (9, 13),
    274: (4, 7),
    273: (15, 19),
    272: (3, 8),
    271: (3, 8),
    270: (17, 20),
    269: (50, 58),
    268: (14, 17),
    267: (16, 19),
    266: (6, 10),
    265: (5, 9),
    264: (8, 12),
    263: (4, 7),
    262: (5, 9),
    261: (4, 7),
    260: (10, 14),
    259: (7, 10),
    258: (17, 19),
    257: (2, 5),
    256: (14, 17),
    255: (4, 7),
    254: (4, 7),
    253: (11, 14),
    252: (17, 21),
    251: (4, 7),
    250: (4, 8),
    249: (13, 16),
    248: (4, 10),
    247: (3, 7),
    246: (6, 9),
    245: (20, 25),
    244: (6, 9),
    243: (12, 15),
    242: (9, 12),
    241: (9, 12),
    240: (3, 7),
    239: (2, 9),
    238: (9, 12),
    237: (7, 11),
    236: (9, 14),
    235: (3, 8),
    234: (4, 6),
    233: (13, 16),
    232: (6, 9),
    231: (12, 15),
    230: (4, 7),
    229: (4, 7),
    228: (7, 10),
    227: (5, 8),
    226: (4, 7),
    225: (12, 15),
    224: (5, 9),
    223: (8, 11),
    222: (3, 6),
    221: (6, 9),
    220: (16, 19),
    219: (5, 7),
    218: (44, 47),
    217: (9, 12),
    216: (3, 7),
    215: (10, 13),
    214: (7, 9),
    213: (3, 6),
    212: (10, 15),
    211: (6, 9),
    210: (5, 8),
    209: (8, 11),
    208: (8, 11),
    207: (7, 10),
    206: (5, 7),
    205: (10, 15),
    204: (6, 9),
    203: (10, 13),
    202: (4, 6),
    201: (17, 19),
    200: (6, 9),
    199: (4, 7),
    198: (12, 16),
    197: (2, 6),
    196: (28, 31),
    195: (7, 10),
    194: (7, 10),
    193: (5, 7),
    192: (21, 23),
    191: (8, 11),
    190: (6, 9),
    189: (4, 7),
    188: (7, 10),
    187: (23, 26),
    186: (19, 22),
    185: (10, 13),
    184: (9, 12),
}


# Process each entry in the dictionary
for video_id, (start_time, end_time) in relevantkickfliptimes.items():
    # Convert times to "HH:MM:SS" format if needed
    start_time = f"00:{start_time // 60:02}:{start_time % 60:02}"
    end_time = f"00:{end_time // 60:02}:{end_time % 60:02}"

    # Construct input and output file paths
    input_video = os.path.join(input_dir, f"{video_id}_kickflip.avi")
    output_video = os.path.join(output_dir, f"{video_id}_regular_kickflip.avi")

    # Check if input video exists
    if not os.path.exists(input_video):
        print(f"Video {input_video} not found. Skipping.")
        continue

    # FFmpeg command to trim the video
    command = [
        "ffmpeg",
        "-i", input_video,
        "-ss", start_time,  # Start time
        "-to", end_time,  # End time
        "-c", "copy",  # Copy codec for fast trimming
        output_video
    ]

    # Execute the FFmpeg command
    try:
        subprocess.run(command, check=True)
        print(f"Trimmed {video_id} saved as {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error trimming {video_id}: {e}")
