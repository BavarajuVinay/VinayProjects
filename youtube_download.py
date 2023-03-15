import pytube
link = input("Enter the video URL: ")
fetch = pytube.YouTube(link)
filter = fetch.streams.filter(progressive=True,file_extension='mp4')
filter.get_highest_resolution().download()
print("Video has been downloaded !")
