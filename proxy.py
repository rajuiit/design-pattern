class RealVideo:
    def __init__(self, video_id):
        self.video_id = video_id
        self.load_video()

    def load_video(self):
        print(f"Loading video {self.video_id} from the server...")

    def play(self):
        print(f"Playing video {self.video_id}.")
class VideoProxy:
    def __init__(self, video_id):
        self.video_id = video_id
        self.real_video = None

    def play(self):
        if not self.real_video:
            print(f"Initializing proxy for video {self.video_id}.")
            self.real_video = RealVideo(self.video_id)
        self.real_video.play()
if __name__ == "__main__":
    # Create a proxy for the video
    proxy = VideoProxy("video123")

    # Play the video for the first time (video will be loaded)
    proxy.play()

    # Play the video again (cached in the proxy)
    proxy.play()
