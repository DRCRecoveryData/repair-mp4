import os
import ffmpeg


def repair_mp4(file_path):
    try:
        # Create the name for the repaired file
        repaired_file = file_path.replace(".mp4", "_repaired.mp4")

        # Repair the MP4 by remuxing it
        ffmpeg.input(file_path).output(repaired_file, vcodec="copy", acodec="copy").run(
            quiet=True, overwrite_output=True
        )

        print(f"Repaired: '{repaired_file}'")

    except Exception as e:
        print(f"Failed to repair '{file_path}': {e}")


def process_directory(root_directory):
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".mp4") and "repaired" not in file.lower():
                file_path = os.path.join(subdir, file)
                repair_mp4(file_path)


if __name__ == "__main__":
    root_directory = "videos"
    process_directory(root_directory)
