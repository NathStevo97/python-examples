from pytube import YouTube
from pytube.cli import on_progress


def main(link):
    yt_object = YouTube(
        link, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress
    )
    yt_object = yt_object.streams.get_highest_resolution()
    try:
        yt_object.download()
    except Exception as e:
        print(f"There was a problem downloading the video: {e}")
    print("Download Completed Successfully!")

if __name__ == "__main__":
    yt_link = input("Enter Youtube yt_link: ")
    if not yt_link.startswith("https://www.youtube.com/watch"):
        print("Please enter a valid YouTube yt_link.")
    else:
        main(yt_link)
        print("Thank you for using the YouTube Downloader!")
