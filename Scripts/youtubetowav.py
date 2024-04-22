from __future__ import unicode_literals
import yt_dlp
import sys
import os

# Create the "music" directory if it doesn't exist
output_dir = "music"
os.makedirs(output_dir, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
    'ffmpeg_location': 'C:\\Users\\matro\\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe',
}


def download_from_url(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_from_file(file_path):
    with open(file_path, 'r') as file:
        links = file.readlines()

    for link in links:
        link = link.strip()
        if link:
            print(f"Downloading: {link}")
            download_from_url(link)


def main():
    args = sys.argv[1:]
    if len(args) > 1:
        print("Too many arguments.")
        print("Usage: python youtubetowav.py <optional link or file>")
        print("If a link is given, it will automatically convert it to .wav.")
        print("If a file path is given, it will download links from the file.")
        print("Otherwise, a prompt will be shown.")
        exit()

    if len(args) == 0:
        url = input("Enter YouTube URL or file path: ")
        if url.endswith(".txt"):
            download_from_file(url)
        else:
            download_from_url(url)
    else:
        if args[0].endswith(".txt"):
            download_from_file(args[0])
        else:
            download_from_url(args[0])


if __name__ == '__main__':
    main()
