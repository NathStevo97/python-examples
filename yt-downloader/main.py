import yt_dlp

def download(url, save_path="downloads"):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
        print(f"Starting download for: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download Completed Successfully!")
    except Exception as e:
        print(f"There was a problem downloading the video: {e}")

if __name__ == "__main__":
    yt_link = input("Enter Youtube link: ")
    if not yt_link.startswith("https://www.youtube.com/watch"):
        print("Please enter a valid YouTube link.")
    else:
        download(yt_link)
        print("Thank you for using the YouTube Downloader!")