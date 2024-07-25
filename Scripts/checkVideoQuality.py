from moviepy.editor import VideoFileClip


def get_video_specs(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        resolution = (video.size[0], video.size[1])
        frame_rate = video.fps
        video.close()

        return {
            "duration": duration,
            "resolution": resolution,
            "frame_rate": frame_rate
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    file_path = input("Enter the path to the video file: ")
    specs = get_video_specs(file_path)

    if "error" in specs:
        print("Error:", specs["error"])
    else:
        print("Video Duration:", specs["duration"])
        print("Resolution:", specs["resolution"])
        print("Frame Rate:", specs["frame_rate"])
