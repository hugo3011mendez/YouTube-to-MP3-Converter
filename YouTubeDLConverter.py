import os
import youtube_dl

exit = False
while exit == False:
    # url input from user
    url = input("Enter the URL of the video you want to download: \n>> ")

    # Specify your download path in the code :)
    download_path = "E:\descargas"

    # YoutubeDL configuration
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Conversion and download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        exit

    # Question regarding the loop
    response = str(input("\033[1;34m Do you want to keep converting videos? y/n \n"))
    if response == "y" :
        exit = False
    elif response == "n" :
        exit = True