import time
import threading

class VideoUploader(threading.Thread):
    def __init__(self, video):
        threading.Thread.__init__(self)
        self.video = video

    def run(self):
        print(f"Uploading ... {self.video}")
        time.sleep(2)
        print(f"Uploaded Successfully {self.video}")

list1 = ["Python programming", "Data Science", "Machine Learning", "Artificial Intelligence", "Deep Learning"]

# t1 = VideoUploader(list1)
# t1.start()
# t1.join()

for video in list1:
    t1 = VideoUploader(video)
    t1.start()
    t1.join()

# def upload_video(video):
#     print(f"Uploading {video}")
#     time.sleep(2)
#     print(f"Uploaded {video}")

# for video in list1:
#     time.sleep(1)
#     upload_video(video)