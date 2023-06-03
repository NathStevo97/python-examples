from pytube import YouTube
from pytube.cli import on_progress

def Download(link):
    youtubeObject = YouTube(link, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There was a problem downloading the video - please try again")
    print("Download Completed Successfully!")

link = input("Enter Youtube link: ")
Download(link)