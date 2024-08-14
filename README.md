# repair-mp4

## Overview

The repair-mp4 script is a tool designed to fix MP4 files that may have become corrupted or otherwise unreadable. By remuxing the video files, it attempts to repair them so they can be played without issues. This script processes all MP4 files in a specified directory, creating a repaired version of each.

## Features

- Batch Processing: Automatically repairs all MP4 files in the specified directory.
- Remuxing: Uses ffmpeg to remux video files, keeping the original video and audio codecs.
- Safe Output: The repaired files are saved with a _repaired suffix, ensuring the originals are not overwritten.

## Usage

1. Clone the repository, navigate to the repair-mp4 directory and download dependencies.

```bash
git clone https://github.com/MoAlkhateeb/repair-mp4.git
cd repair-mp4
pipenv install
```

2. Prepare Your Directory:
Place all the MP4 files you wish to repair in a directory named videos or update the root_directory variable in the script to point to your desired directory.


3. Run the Script:

```bash
python main.py
```

4. Output: 
The script will create a repaired version of each MP4 file in the same directory, appending _repaired to the filename.

## Notes
- The script processes all MP4 files in the specified directory, excluding those already labeled as repaired.
- Keep backups of your original files, as this script does not overwrite them but creates new versions.

## Contributing
Feel free to open issues or submit pull requests to improve the script or add new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.