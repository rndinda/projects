from pytube import YouTube
from sys import argv

# to run from the command line and be able to access link from command
link = argv[1]
yt_link = YouTube(link)

# to get the title of the video
print("Title: ", yt_link.title)

# to get the current views on the video
print("View: ", yt_link.views)

# to download the best resolution of the video
yt_d = yt_link.streams.get_highest_resolution()

# to download and store
yt_d.download('/Users/User/Desktop/youtube downnloads')