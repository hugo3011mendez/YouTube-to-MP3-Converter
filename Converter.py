# importing packages
from pytube import YouTube
import os
import subprocess

# Loop for converting more than one video
exit = False
while exit == False:
	# url input from user
	yt = YouTube(
		str(input("Enter the URL of the video you want to download: \n>> ")))


	# Extract only audio
	fileStream = yt.streams.filter(only_audio=True).first() # Obtains the stream of video or in this case, the audio


	# Check for destination to save file

	# print("Enter the destination (leave blank for current directory)")
	# destination = str(input(">> ")) or '.'

	# No need for destination input because my destination will be always the same
	destination = "E:\descargas"


	# Download the file
	out_fileName = fileStream.download(output_path = destination) # Returns the name of the downloaded file


	# Save the file
	baseName, fileExtension = os.path.splitext(out_fileName) # Splits the file name and its extension
	command = 'ffmpeg -i "' + out_fileName + '" "' + baseName + '.mp3"' # Establishes the command to run in the command console
	subprocess.run(command, shell=True, capture_output=True) # Converts the file to MP3
	# TODO : Find a way to download the mp3 without downloading and deleting the mp4 afterwards
	os.remove(out_fileName) # Deletes the downloaded mp4 which we don't want

	# Result output of success
	print("\033[1;32m " + yt.title + " has been successfully downloaded!")

	# Question regarding the loop
	response = str(input("\033[1;34m Do you want to keep converting videos? y/n \n"))
	if response == "y" :
		exit = False
	elif response == "n" :
		exit = True