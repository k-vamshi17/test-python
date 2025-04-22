from pytube import YouTube

def download_youtube_video(video_url):
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Print video title
        print(f"Downloading: {yt.title}")

        # Select the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download()

        print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Input the YouTube video link
    video_link = input("Enter the YouTube video URL: ")
    download_youtube_video(video_link)
