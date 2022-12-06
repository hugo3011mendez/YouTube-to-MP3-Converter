# importing packages
from pytube import YouTube
import os


# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))


# extract only audio
fileStream = yt.streams.filter(only_audio=True).first() # Obtains the stream of video or in this case, the audio


# check for destination to save file

# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'

# No need for destination input because my destination will be always the same
destination = "E:\descargas"


# download the file
out_fileName = fileStream.download(output_path = destination) # Returns the name of the downloaded file


# save the file
baseName, fileExtension = os.path.splitext(out_fileName) # Splits the file name and its extension
mp3_file = baseName + '.mp3' # Establishes the new file extension
os.rename(out_fileName, mp3_file) # And renames the file


# result of success
print(yt.title + " has been successfully downloaded!")