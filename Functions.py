import os
import datetime
import yt_dlp

def set_file_modification_time(file_path):
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Convert the timestamp to the number of seconds since the epoch
    timestamp = current_time.timestamp()

    # Set the file's modification time
    os.utime(file_path, (timestamp, timestamp))


def download_audio(url, output_dir):
    # YoutubeDL configuration
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'prefer_ffmpeg': True,
        'keepvideo': False
    }

    # Conversion and download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict['title']
        output_file = os.path.join(output_dir, f'{video_title}.mp3')

        ydl.download([url])

    # Set the modification time of the output file
    set_file_modification_time(output_file)

    print('Conversion completed!')