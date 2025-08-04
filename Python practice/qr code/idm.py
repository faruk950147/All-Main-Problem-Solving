from yt_dlp import YoutubeDL

# url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
# output_path = "Downloads/%(title)s.%(ext)s"

# ydl_opts = {"outtmpl": output_path}
# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])

# print("Done")


import os

def download(url, output_path):
    if url and output_path:
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Folder create
            ydl_opts = {
                "format": "best", # best format
                "live_from_begin": True, # live from begin
                "quiet": False, # progress show
                "outtmpl": output_path, # output path
                "merge_output_format": "mp4", # merge output format
            }
            print("Downloading...")
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Download Completed Successfully!")
        except Exception as e:
            print("Download Failed:", str(e))
    else:
        print("Invalid URL or Output Path")

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
output_path = "Downloads/%(title)s.%(ext)s"
download(url, output_path)
