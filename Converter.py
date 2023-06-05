from Functions import download_audio

exit = False
while exit == False:
    # url input from user
    url = input("Enter the URL of the video you want to download: \n>> ")

    # Specify your download path in the code :)
    download_path = "E:\\descargas\\"

    download_audio(url, download_path)

    # Question regarding the loop
    response = str(input("\033[1;34m Do you want to keep converting videos? y/n \n"))
    if response == "y" :
        exit = False
    elif response == "n" :
        exit = True