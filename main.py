import os
import ffmpeg
import argparse

def repair_mp4(file_path, output_dir):
    try:
        # Create the name for the repaired file
        repaired_file = os.path.join(output_dir, os.path.basename(file_path))

        # Repair the MP4 by remuxing it
        ffmpeg.input(file_path).output(repaired_file, vcodec="copy", acodec="copy").run(
            quiet=True, overwrite_output=True
        )

        print(f"Repaired: '{repaired_file}'")

    except Exception as e:
        print(f"Failed to repair '{file_path}': {e}")

def process_directory(root_directory, output_dir):
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.lower().endswith(".mp4") and "repaired" not in file.lower():
                file_path = os.path.join(subdir, file)
                repair_mp4(file_path, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Repair MP4 files.")
    parser.add_argument("input_path", help="Path to the file or directory to process")
    parser.add_argument("output_dir", help="Directory to save repaired files")

    args = parser.parse_args()

    input_path = args.input_path
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.isdir(input_path):
        process_directory(input_path, output_dir)
    else:
        repair_mp4(input_path, output_dir)
