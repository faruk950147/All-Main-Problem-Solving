import time
import threading
class VideoUploader(threading.Thread):
    def __init__(self, video):
        threading.Thread.__init__(self)
        self.video = video
    def run(self):
        print(f"Uploading {self.video}")
        time.sleep(2)
        print(f"Uploaded {self.video}")
list1 = ["Python programming", "Data Science", "Machine Learning", "Artificial Intelligence", "Deep Learning"]

for video in list1:
    time.sleep(1)
    VideoUploader(video).start()
    print("Copyright @")

# def upload_video(video):
#     print(f"Uploading {video}")
#     time.sleep(2)
#     print(f"Uploaded {video}")

# for video in list1:
#     time.sleep(1)
#     upload_video(video)