from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There was a problem downloading the video - please try again")
    print("Download Completed Successfully!")

link = input("Enter Youtube link: ")
Download(link)